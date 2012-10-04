import web

urls = (
		'/', 'index'
		)

render = web.template.render('templates', base='layout')

class index:
	""" index of site """
	def GET(self):
		return render.index()
app = web.application(urls, globals())
app = app.gaerun()

