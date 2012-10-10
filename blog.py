import web
from google.appengine.ext import db
from models import Post
from google.appengine.api import users

urls = (
		#'', 'reblog',
		'/?$', 'index',
		'/create/?$', 'create',
		'/p/([^/]*)/?$', 'post'
		)

globals = { 'users' : users }

shared = web.template.render('templates/shared')
render = web.template.render('templates/blog', globals=globals)

class reblog:
    def GET(self):
        def GET(self): raise web.seeother('/')

class index:
	def GET(self):
		#get latest 3 blog posts
		q = Post().all()
		posts = q.run(limit=3)
		
		return shared.layout(render.index(posts, ))

class create:
	def GET(self):
		if users.is_current_user_admin():
			return shared.layout(render.create(self))
		else:
			raise web.Forbidden()

	def POST(self):
		pass

app_blog = web.application(urls, locals())
