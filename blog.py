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
		posts = Post.query().fetch(3)
		
		dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
		posts_json = map(lambda p: json.dumps(p.to_dict(), default=dthandler), posts)

		return render.index(posts=posts, posts_json=posts_json)

class post:
	def GET(self, key):
		post = ndb.Key(urlsafe=key).get()
		return render.post(post=post)

