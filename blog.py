import web
from web.contrib.template import render_mako
from models import Category, Entry
from google.appengine.ext import ndb
from datetime import datetime, timedelta

urls = (
		'^/?$', 'index',
		'/([\w\d-]+)/?', 'entry',
		'/(\d{4})/(\d{2})/(\d{2})/([-\w\d]+)/?', 'fetchByDate',
		'/category/([\w\d]+)/?', 'category'
		)

render = render_mako(
		directories=['templates/shared', 'templates/blog'],
		input_encoding='utf-8',
		output_encoding='utf-8',
		)

app = web.application(urls, locals())

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
		q = Entry.query(Entry.published==True).order(-Entry.timestamp)
		entries = q.fetch(3, projection=[Entry.title, Entry.timestamp, Entry.intro])
		e_list = q.fetch(5, projection=[Entry.title])

		categories = Category.query().order(Category.name).fetch()
		
		data = {
			'entries' : entries,
			'categories': categories,
			'e_list': e_list
		}

		return render.index(**data)

class entry:
	def GET(self, key):
		entry = ndb.Key(urlsafe=key).get()
		q = Entry.query(Entry.published==True).order(-Entry.timestamp)
		entries = q.fetch(3, projection=[Entry.title, Entry.timestamp, Entry.intro])
		e_list = q.fetch(5, projection=[Entry.title])
		
		categories = Category.query().order(Category.name).fetch()

		data = {
				'entry': entry,
				'categories': categories,
				'e_list': e_list
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
			categories = Category.query().order(Category.name).fetch()
			e_list = q.fetch(3, projection=[Entry.title, Entry.timestamp, Entry.intro])
		
			data = {
				'entry': entry[0],
				'categories': categories,
				'e_list': []
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
			entries = q.filter(Entry.category==c[0].key).fetch(3, projection=[Entry.title, Entry.timestamp, Entry.intro])
			e_list = q.fetch(5, projection=[Entry.title])

			categories = Category.query().order(Category.name).fetch()
			
			data = {
				'entries' : entries,
				'categories': categories,
				'e_list': e_list
			}

			return render.index(**data)
