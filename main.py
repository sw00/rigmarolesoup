import web
import admin
import blog
from web.contrib.template import render_mako

urls = (
		'/', 'index',
		'/admin', admin.app_admin,
		'/blog', blog.app_blog,
		)

render= render_mako(
		directories=['templates'],
		input_encoding='utf-8',
		output_encoding='utf-8',
		)

class index:
	""" handler for landing page """
	def GET(self):
		return render.index()


app = web.application(urls, globals())
app = app.gaerun()

