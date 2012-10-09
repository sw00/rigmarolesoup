import web
from google.appengine.ext import db
from models import Post

urls = (
		'', 're_index',
		'/', 'index',
		'/blog', 'blog'
		)

shared = web.template.render('templates/shared')
render = web.template.render('templates/admin')

class re_index:
    def GET(self): raise web.seeother('/')

class index:
	def GET(self):
		return shared.layout(render.index())

class blog:
	def GET(self):
		q = Post().all()
		q.order('created')
		posts = q.run(limit=10)
		return shared.layout(render.blog(posts))

app_admin = web.application(urls, globals())

