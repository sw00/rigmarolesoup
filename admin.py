import web

urls = (
		'', 're_index',
		'/', 'index',
		'/blog', 'blog'
		)

render = web.template.render('templates/admin')

class re_index:
    def GET(self): raise web.seeother('/')

class index:
	def GET(self):
		return render.index()

class blog:
	def GET(self):
		return render.blog()

app_admin = web.application(urls, globals())

