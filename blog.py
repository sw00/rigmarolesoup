import web
from web.contrib.template import render_mako
from web import form
from models import Post
from models import Category
from google.appengine.ext import ndb
from google.appengine.api import users
import json
import datetime

urls = (
		'^/?$', 'index',
		'/list/(\w+)/?$', 'list',
		'/create/(\w+)/?$', 'create',
		'/p/([a-zA-Z0-9-]+)/?', 'post'
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
		posts = Post.fetch_all().fetch(3)
		
		dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
		posts_json = map(lambda p: json.dumps(p.to_dict(), default=dthandler), posts)

		return render.index(posts=posts, posts_json=posts_json)

class post:
	def GET(self, name):
		p_key = ndb.Key(urlsafe=name)
		return render.post(post=p_key.get())


class list:
	@authorise
	def GET(self, name):
		if name.lower() == 'category':
			q = Category.query().order(Category.name)
			results, cursor, more = q.fetch_page(10)

			if cursor: cursor = cursor.urlsafe()

			return render.list(categories=results, cursor=cursor, more=more)
		elif name.lower() == 'post':
			q = Post.query().order(Post.created) 
			results,cursor,more = q.fetch_page(10, projection=[
				Post.created,
				Post.title,
				Post.published])
			
			if cursor: cursor = cursor.urlsafe()

			return render.list(posts=results, cursor=cursor, more=more)
		else:
			raise web.badrequest()

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
			form.Textarea('references',form.regexp(
				r'\b|http://[a-zA-Z.\d/#?&]*|www.[a-zA-Z.\d/#?&]*',
				'Invalid URL(s) entered.'
				), rows='4', cols='80'),
			form.Textbox('tags', form.regexp(
				r'\b|w+|-', 
				'Invalid tag(s) entered.')
				),
			form.Button('submit', type='submit')
			)

		return createform

	@classmethod
	def consume_post_form(cls, form_d):
		references = form_d.references.value.split('\n')
		references = map(lambda x: x.strip(), references)

		category = form_d.category.value
		if category:
			category = ndb.Key(urlsafe=category)

		tags = form_d.tags.value.split(' ')
		tags = map(lambda x: x.strip(), tags)

		post = Post(
				title = form_d.title.value,
				body = form_d.content.value,
				references = references,
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
				form.Button('submit', type='submit')
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
		if name == 'p':
			form = self.create_post_form()
			title = 'New Blog Post'
			name = 'post'
			mce_elms.append('content')
		elif name == 'c':
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

