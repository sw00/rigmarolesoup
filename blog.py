import web

urls = (
		#'', 'reblog',
		'/?$', 'index',
		'/post/([^/]*)/?$', 'post'
		)

render = web.template.render('templates/blog')

class reblog:
    def GET(self):
        def GET(self): raise web.seeother('/')

class index:
	def GET(self):
		return render.index()

class post:
    def GET(self, alias):
        return alias

app_blog = web.application(urls, locals())
