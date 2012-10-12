import web
from web.contrib.template import render_mako
from web import form
from models import Post
from models import Category
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

app_blog = web.application(urls, locals())

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
	@classmethod
	def create_form(cls):
		#fetch the categories:
		q = Category.query().order(Category.name)
		categories = q.fetch(10)

		createform = form.Form(
			form.Textbox('title'),
			form.Dropdown('category', map(lambda x: (x.key, x.name), categories)), 
			form.Textarea('content'),
			form.Textarea('references',form.regexp(
				r'http://[a-zA-Z.\d/#?&]*|www.[a-zA-Z.\d/#?&]*',
				'Invalid URL(s) entered.'
				), rows='4', cols='80'),
			form.Textbox('tags', form.regexp(
				r'\w+|-', 
				'Invalid tag(s) entered.')
				),
			form.Button('submit', type='submit')
			)

		return createform

	@classmethod
	def consume_form(cls, form_d):
		references = form_d.references.value.split('\n')
		references = map(lambda x: x.strip(), references)

		#todo fetch the parent (category)
		#category_key = ndb.Key(urlsafe=form_d.category.value)
		#category = category_key.get()
		category = form_d.category.value

		tags = form_d.tags.value.split(' ')
		tags = map(lambda x: x.strip(), tags)

		post = Post(
				title = form_d.title.value,
				body = form_d.content.value,
				references = references,
				category = category,
				tags = tags)

		post.put()

	def GET(self):
		if users.is_current_user_admin():
			form = self.create_form()
			return render.create(form=form)
		else:
			raise web.Forbidden()

	def POST(self):
		#todo: CREATE post object and persist in data store.
		if not users.is_current_user_admin():
			raise web.Forbidden()

		form = self.create_form()
		if not form.validates():
			return render.create(form=form)
		else:
			p = self.consume_form(form)
			#return render.preview(form.d)
			raise web.seeother('/blog') 

