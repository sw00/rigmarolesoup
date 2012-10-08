import web
import admin
import blog

urls = (
		'/', 'index',
		'/admin', admin.app_admin,
		'/blog', blog.app_blog,
		)

render = web.template.render('templates', base='layout')

class index:
	""" index of site """
	def GET(self):
		return render.index()

app = web.application(urls, globals())
app = app.gaerun()

