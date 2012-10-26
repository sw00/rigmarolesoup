import web
import blog
import api
from web.contrib.template import render_mako

urls = (
		'/', 'index',
		'/blog', blog.app_blog,
		'/api', api.app
		)

render= render_mako(
		directories=['templates/shared', 'templates'],
		input_encoding='utf-8',
		output_encoding='utf-8',
		)

class index:
	""" handler for landing page """
	def GET(self):
		return render.index()


app = web.application(urls, globals())
app = app.gaerun()

