import web
from web.contrib.template import render_mako
from web import form
from models import Entry as Post
from models import Category
from google.appengine.ext import ndb
from google.appengine.api import users
import json
import datetime

urls = (
		'^/?$', 'index',
		'/p/(.*)/?$', 'post',
		'/list/?$', 'relist',
		'/list/(\w+)/?$', 'list',
		'/create/(\w+)/?$', 'create',
		'/edit/(.*)/?$|/?$', 'update',
		'/delete/(.*)/?$|/?$', 'delete'
		)

render = render_mako(
		directories=['templates/shared', 'templates/blog'],
		input_encoding='utf-8',
		output_encoding='utf-8',
		)

app_blog = web.application(urls, locals())

def authorise(func):
	def decorate(*args, **kwargs):
		if not users.is_current_user_admin():
			raise web.forbidden()
		else:
			return func(*args, **kwargs)
	return decorate

class index:
	def GET(self):
		#get latest 3 blog posts
		posts = Post.query().fetch(3)
		
		dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
		posts_json = map(lambda p: json.dumps(p.to_dict(), default=dthandler), posts)

		return render.index(posts=posts, posts_json=posts_json)

class post:
	def GET(self, key):
		post = ndb.Key(urlsafe=key).get()
		return render.post(post=post)

class relist:
	@authorise
	def GET(self):
		if not users.is_current_user_admin():
			raise web.seeother(users.create_login_url('/blog/list/post'))
		else:
			raise web.seeother('/list/post')

class list:
	@authorise
	def GET(self, name):
		if name.lower() == 'category':
			q = Category.query().order(Category.name)
			results, cursor, more = q.fetch_page(10)

			if cursor: cursor = cursor.urlsafe()

			return render.list(categories=results, cursor=cursor, more=more)
		elif name.lower() == 'post':
			q = Post.query().order(Post.timestamp) 
			results,cursor,more = q.fetch_page(10, projection=[
				Post.timestamp,
				Post.title,
				Post.published])
			
			if cursor: cursor = cursor.urlsafe()

			return render.list(posts=results, cursor=cursor, more=more)
		else:
			raise web.seeother('/blog/list/post')

class create:
	@classmethod
	def create_post_form(cls):
		#fetch the categories:
		q = Category.query().order(Category.name)
		categories = q.fetch(10)

		createform = form.Form(
			form.Checkbox('published', value=True, checked='checked'),
			form.Textbox('title'),
			form.Dropdown('category', map(lambda x: (x.key.urlsafe(), x.name), categories)), 
			form.Textarea('content'),
			form.Textbox('tags', form.regexp(
				r'^$|\w+|-', 
				'Invalid tag(s) entered.')
				),
			form.Button('submit', type_='submit', class_='btn btn-primary btn-large')
			)

		return createform

	@classmethod
	def consume_post_form(cls, form_d):
		category = form_d.category.value
		if category:
			category = ndb.Key(urlsafe=category)

		tags = form_d.tags.value.split(' ')
		tags = map(lambda x: x.strip(), tags)

		post = Post(
				title = form_d.title.value,
				content = form_d.content.value,
				tags = tags,
				published = form_d.published.value,
				parent = category)
		
		return post.put()

	@classmethod
	def create_category_form(cls):
		createform = form.Form(
				form.Textbox('name', form.regexp(
					r'[a-zA-Z ]', 'Invalid chars entered.')),
				form.Textbox('desc'),
				form.Button('submit', type_='submit', class_='btn btn-primary btn-large')
				)

		return createform

	@classmethod
	def consume_category_form(cls, form_d):
		c = Category(
				name = form_d.name.value,
				desc = form_d.desc.value
				)
		
		return c.put()	
	

	@authorise
	def GET(self, name):
		if name == 'post':
			form = self.create_post_form()
			title = 'New Blog Post'
		elif name == 'category':
			form = self.create_category_form()
			title = 'New Blog Category'
		else:
			raise web.badrequest()
		
		return render.create(title=title,form=form,mce_elms='content')

	@authorise
	def POST(self, name):
		mce_elms = []
		if name == 'post':
			form = self.create_post_form()
			title = 'New Blog Post'
			name = 'post'
			mce_elms.append('content')
		elif name == 'category':
			form = self.create_category_form()
			title = 'New Blog Category'
			name = 'category'
		else:
			raise web.badrequest()
			
		if not form.validates():
			return render.create(title=title,mce_elms=mce_elms,form=form)
		else:
			method = 'consume_' + name + '_form'
			getattr(self, method)(form)
			raise web.seeother('/list') 

class delete:
	@classmethod
	def create_delete_form(cls, key): 
		return form.Form(
			form.Hidden('key', value=key),
			form.Button('submit', type_='submit'),
			form.Button('cancel', type_='cancel')
			)

	@authorise
	def GET(self, key): 
		form = self.create_delete_form(key)
		return render.delete(form=form)
		
	@authorise
	def POST(self, key):
		form = self.create_delete_form(key)
		m = ndb.Key(urlsafe=form.key.value)
		m.delete()

		raise web.seeother('/blog/list', True)

class update:
	@classmethod
	def create_update_form(cls, entity=None):
		if entity.key.kind() == 'Post':
			q = Category.query().order(Category.name)
			categories = q.fetch(10)

			createform = form.Form(
				form.Checkbox('published', value=entity.published, checked='checked'),
				form.Textbox('title', value=entity.title),
				form.Dropdown('category', map(lambda x: (x.key.urlsafe(), x.name), categories)), 
				form.Textarea('content', value=entity.content),
				form.Textbox('tags', form.regexp(
					r'^$|\w+|-', 
					'Invalid tag(s) entered.'),
					value=reduce(lambda x,y: x + ' ' + y, entity.tags)
					),
				form.Button('submit', type_='submit', class_='btn btn-primary btn-large')
				)
		elif entity.key.kind() == 'Category':
			createform = form.Form(
				form.Textbox('name', form.regexp(
					r'[a-zA-Z ]', 'Invalid chars entered.'),
					value=entity.name),
				form.Textbox('desc', value=entity.desc),
				form.Button('submit', type_='submit', class_='btn btn-primary btn-large')
				)

		return createform


	@authorise
	def GET(self, key):
		entity = ndb.Key(urlsafe=key).get()
		form = self.create_update_form(entity)

		return render.update(form=form, title='Update %s' % entity.key.kind(), mce_elms='content')

	@authorise
	def POST(self, key):
		entity = ndb.Key(urlsafe=key).get()
		form = self.create_update_form(entity)
		
		if form.validates():
			if entity.key.kind() == 'Post':
				entity.title = form.title.value
				entity.content = form.content.value
				entity.tags = form.tags.value.split(' ')
				entity.published = form.published.value

				entity.put()
				return web.seeother('/blog/list/post', True)
			elif entity.key.kind() == 'Category':
				entity.name = form.name.value
				entity.desc= form.desc.value
				
				entity.put()
				return web.seeother('/blog/list/category', True)
			else:
				return web.badrequest()

