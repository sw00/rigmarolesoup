import web
from google.appengine.ext import db
from models import Post

urls = (
		#'', 'reblog',
		'/?$', 'index',
		'/p/([^/]*)/?$', 'post'
		)

shared = web.template.render('templates/shared')
render = web.template.render('templates/blog')

class reblog:
    def GET(self):
        def GET(self): raise web.seeother('/')

class index:
	def GET(self):
		#get latest 3 blog posts
		q = Post().all()
		posts = q.run(limit=3)

		return shared.layout(render.index(posts))

class post:
    def GET(self, alias):
        return alias

app_blog = web.application(urls, locals())
