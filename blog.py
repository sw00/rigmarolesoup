import web
from web import form
from google.appengine.ext import db
from models import Post
from google.appengine.api import users

urls = (
		#'', 'reblog',
		'/?$', 'index',
		'/create/?$', 'create',
		'/p/([^/]*)/?$', 'post'
		)

shared = web.template.render('templates/shared')

globals = { 
			'users' 	: users
			}
shared = web.template.render('templates/shared', globals=globals)
globals['template'] = shared
render = web.template.render('templates/blog', globals=globals)

class reblog:
    def GET(self):
        def GET(self): raise web.seeother('/')

class index:
	def GET(self):
		#get latest 3 blog posts
		q = Post().all()
		posts = q.run(limit=3)
		
		return shared.layout(render.index(posts))


class create:
	createform = form.Form(
			form.Textbox('title'),
			form.Dropdown('category', [('0', 'None')]),
			form.Textarea('content'),
			form.Textbox('references'),
			form.Textbox('tags'),
			form.Button('submit', type='submit')
			)

	def GET(self):
		if users.is_current_user_admin():
			form = self.createform()
			return shared.layout(render.create(form))
		else:
			raise web.Forbidden()

	def POST(self):
		form = self.createform()
		if not form.validates():
			return shared.layout(render.create(form))
		else:
			return shared.layout(render.preview(form.d))

app_blog = web.application(urls, locals())
