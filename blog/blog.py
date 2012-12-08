import web
from web.contrib.template import render_mako
from models import Category, Entry
from google.appengine.ext import ndb
from datetime import datetime, timedelta
from lib.markdown2 import markdown

urls = (
		'^/?$', 'index',
		'/([\w\d-]+)/?', 'entry',
		'/(\d{4})/(\d{1,2})/(\d{1,2})/([-\w\d]+)/?', 'fetchByDate',
		'/category/([\w\d]+)/?', 'category'
		)

render = render_mako(
		directories=['templates/shared', 'templates/blog'],
		input_encoding='utf-8',
		output_encoding='utf-8',
		strict_undefined=True
		)

app = web.application(urls, globals())
app = app.gaerun()

def authorise(func):
	def decorate(*args, **kwargs):
		if not users.is_current_user_admin():
			raise web.forbidden()
		else:
			return func(*args, **kwargs)
	return decorate

def extend_entry(entries, category=False):
	'''Extends each entry object with url attribute
	   Uses flag to determine if category should be extended too
	'''
	for e in entries:
		d  = e.timestamp
		e.url = '%s/%s/%s/%s' % (d.year, d.month, d.day, e.alias)

		if category:
			e.category_name = e.category.get().name

	return entries

categories = Category.query().order(Category.name)
e_list = Entry.query(Entry.published==True).order(-Entry.timestamp)

class index:
	def GET(self):
		#get latest 3 blog posts
		q = Entry.query(Entry.published==True).order(-Entry.timestamp)
		entries = q.fetch(3)

		data = {
			'entries' : extend_entry(entries, True),
			'categories': categories.fetch(),
			'e_list': extend_entry(e_list.fetch(5, projection=[Entry.title, Entry.alias, Entry.timestamp]))
		}

		return render.index(**data)

class entry:
	def GET(self, key):
		entry = ndb.Key(urlsafe=key).get()
		q = Entry.query(Entry.published==True).order(-Entry.timestamp)

		data = {
				'entry': extend_entry(entry, true)
				}

		return render.entry(**data)

class fetchByDate:
	def GET(self, year, month, day, title):
		d = datetime(int(year),int(month),int(day))
		m = timedelta(days=1)

		q = Entry.query(Entry.published==True)
		entry = q.filter(Entry.timestamp >= d, Entry.timestamp <= d+m, Entry.alias==title).fetch(1)

		if len(entry) == 0:
			raise web.notfound()
		else:
			#get category name:
			entry[0].category_name = entry[0].category.get().name

			data = {
				'entry': entry[0],
				'categories': categories.fetch(),
				'e_list': extend_entry(e_list.fetch(5, projection=[Entry.title, Entry.alias, Entry.timestamp]))
				}

			return render.entry(**data)

class category:
	def GET(self, name):
		#get latest 3 blog posts
		c = Category.query(Category.name ==name).fetch(1)
		
		if len(c) == 0:
			raise web.notfound()
		else:
			q = Entry.query(Entry.published==True).order(-Entry.timestamp)
			entries = q.filter(Entry.category==c[0].key).fetch(3)

			for e in entries:
				e.category_name = name

			data = {
				'entries' : extend_entry(entries),
				'categories': categories.fetch(),
				'e_list': extend_entry(e_list.fetch(5, projection=[Entry.title, Entry.alias, Entry.timestamp]))
			}

			return render.index(**data)
