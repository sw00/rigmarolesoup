import web
from web.contrib.template import render_mako
from models import Category, Entry
from google.appengine.ext import ndb

urls = (
		'^/?$', 'index',
		'/p/(.*)/?$', 'post'
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
		
		data = {
			'entries' : Entry.query().fetch(3),
			'categories': Category.query().fetch()
		}

		return render.index(**data)

class post:
	def GET(self, key):
		post = ndb.Key(urlsafe=key).get()
		return render.post(post=post)

