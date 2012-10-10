import web
import admin
import blog

urls = (
		'/', 'index',
		'/admin', admin.app_admin,
		'/blog', blog.app_blog,
		)

class index:
	""" index of site """
	def GET(self):
		shared = web.template.render('templates/shared')
		globals = {
			'template' : shared
			}
		render = web.template.render('templates', globals=globals)
		return shared.layout(render.index(self))

app = web.application(urls, globals())
app = app.gaerun()

