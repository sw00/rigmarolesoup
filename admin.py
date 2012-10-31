import web
from web.contrib.template import render_mako
from web import form
from models import Entry 
from models import Category
from google.appengine.ext import ndb
from google.appengine.api import users
import json
import datetime

urls = (
		'^/?$', 'index',
		#'/list/?$', 'relist',
		'/list/(\w+)/?$', 'list',
		'/create/(\w+)/?$', 'create',
		'/edit/(.*)/?$', 'update',
		'/delete/(.*)/?$', 'delete'
		)

render = render_mako(
		directories=['templates/shared', 'templates/admin'],
		input_encoding='utf-8',
		output_encoding='utf-8',
		)

app = web.application(urls, locals())

def create_form(entity):
	if entity.__class__.__name__ == 'Entry':
		q = Category.query().order(Category.name)
		categories = q.fetch(10)
		
		try:
			tags = reduce(lambda x,y: x + ' ' + y, entity.tags)
		except:
			tags = ''
		
		createform = form.Form(
			form.Checkbox('published', value=entity.published, checked='checked'),
			form.Textbox('title', value=entity.title),
			form.Dropdown('category', map(lambda x: (x.key.urlsafe(), x.name), categories)), 
			form.Textarea('content', value=entity.content),
			form.Textbox('tags', form.regexp(
				r'^$|\w+|-', 
				'Invalid tag(s) entered.'),
				value=tags
				),
			form.Button('submit', type_='submit', class_='btn btn-primary btn-large')
			)
	elif entity.__class__.__name__ == 'Category':
		createform = form.Form(
			form.Textbox('name', form.regexp(
				r'[a-zA-Z ]', 'Invalid chars entered.'),
				value=entity.name),
			form.Textbox('desc', value=entity.desc),
			form.Button('submit', type_='submit', class_='btn btn-primary btn-large')
			)

	return createform

def consume_form(entity, form_d):
		del form_d['submit']

		for k in form_d.keys():
			if k == 'tags':
				form_d[k] = form_d[k].split(' ')

			setattr(entity, k, form_d[k])

		return entity

class index:
	def GET(self):
		return render.index()

class list:
	def GET(self, name):
		if name.lower() == 'category':
			q = Category.query().order(Category.name)
			results, cursor, more = q.fetch_page(10)

			if cursor: cursor = cursor.urlsafe()

			return render.list(categories=results, cursor=cursor, more=more)
		elif name.lower() == 'entry':
			q = Entry.query().order(Entry.timestamp) 
			results,cursor,more = q.fetch_page(10, projection=[
				Entry.timestamp,
				Entry.title,
				Entry.published])
			
			if cursor: cursor = cursor.urlsafe()

			return render.list(posts=results, cursor=cursor, more=more)
		else:
			raise web.seeother('/admin')

class create:
	def GET(self, name):
		if name == 'entry':
			form = create_form(Entry())
			title = 'New Blog Entry'
			mce_elms = ['content']
		elif name == 'category':
			form = create_form(Category())
			title = 'New Blog Category'
			mce_elms = []
		else:
			raise web.badrequest()
		
		return render.form(title=title,form=form,mce_elms=mce_elms)

	def POST(self, name):
		if name == 'entry':
			entity = Entry()
			title = 'New Blog Entry'
			mce_elms = ['content']
		elif name == 'category':
			entity = Category()
			title = 'New Blog Category'
		else:
			raise web.badrequest()

		form = create_form(entity)
			
		if not form.validates():
			return render.form(title=title,mce_elms=mce_elms,form=form)
		else:
			entity = consume_form(entity, form._get_d())
			entity.put()
			raise web.seeother('/list/%s' % name) 

class update:
	def GET(self, key):
		entity = ndb.Key(urlsafe=key).get()
		form = create_form(entity)

		return render.form(form=form, title='Update %s' % entity.key.kind(), mce_elms='content')

	def POST(self, key):
		entity = ndb.Key(urlsafe=key).get()
		form = create_form(entity)
		
		if form.validates():
			if entity.key.kind() == 'Entry':
#				entity.title = form.title.value
#				entity.content = form.content.value
#				entity.tags = form.tags.value.split(' ')
#				entity.published = form.published.value
				
				entity = consume_form(entity, form._get_d())
				entity.put()
				return web.seeother('/list/entry')
			elif entity.key.kind() == 'Category':
				entity.name = form.name.value
				entity.desc= form.desc.value
				
				entity.put()
				return web.seeother('/list/category')
			else:
				return web.badrequest()


class delete:
	@classmethod
	def create_delete_form(cls, key): 
		return form.Form(
			form.Hidden('key', value=key),
			form.Button('submit', type_='submit'),
			form.Button('cancel', type_='cancel')
			)

	def GET(self, key): 
		form = self.create_delete_form(key)
		return render.delete(form=form)
		
	def POST(self, key):
		form = self.create_delete_form(key)
		m = ndb.Key(urlsafe=form.key.value)
		name = m.kind().lower()
		m.delete()

		raise web.seeother('/list/%s' % name)
