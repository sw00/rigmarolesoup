import web
from web.contrib.template import render_mako
from web import form
from models import Post
from google.appengine.ext import ndb
from google.appengine.api import users

urls = (
		#'', 'reblog',
		'/?$', 'index',
		'/create/?$', 'create',
		'/p/([^/]*)/?$', 'post'
		)

render = render_mako(
		directories=['templates/shared', 'templates/blog'],
		input_encoding='utf-8',
		output_encoding='utf-8',
		)

class reblog:
    def GET(self):
        def GET(self): raise web.seeother('/')

class index:
	def GET(self):
		#get latest 3 blog posts
		posts = Post.fetch_all().fetch(3)

		#do the admin check
		login_url = None
		logout_url = None
		if users.is_current_user_admin():
			logout_url = users.create_logout_url('/blog')
		else:
			login_url = users.create_login_url('/blog')

		return render.index(posts=posts, login_url=login_url, logout_url=logout_url)

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
			return render.create(form=form)
		else:
			raise web.Forbidden()

	def POST(self):
		#todo: CREATE post object and persist in data store.
		form = self.createform()
		if not form.validates():
			return shared.layout(render.create(form))
		else:
			return shared.layout(render.preview(form.d))

app_blog = web.application(urls, locals())
