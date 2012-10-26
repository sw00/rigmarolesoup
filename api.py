import web
import json
import datetime
from web.contrib.template import render_mako
from models import Entry, Category
from google.appengine.ext import ndb
from google.appengine.api import users

urls = (
		'/entry/(.*)/?', 'EntryController',
		'/category/(.*)/?', 'CategoryController',
		)

render = render_mako(
		directories=['templates/shared', 'templates/blog', 'templates/blog/models'],
		input_encoding='utf-8',
		output_encoding='utf-8'
		)

app = web.application(urls, locals())

def authorise(func):
	def decorate(*args, **kwargs):
		if not users.is_current_user_admin():
			raise web.forbidden()
		else:
			return func(*args, **kwargs)
	return decorate


class Controller:
	'''Generic controller base class using REST principles
	'''

	entity = None

	def __init__(self, entity):
		self.entity = entity.__class__

	def GET(self, key=None):
		model = ndb.Key(urlsafe=key).get()
		
		model_json = self._json(model)  #converts model to json string

		template = self.entity.__name__
		data = {
				'model' : model,
				'json' : model_json
				}

		return getattr(render, template)(**data)

	@authorise
	def POST(self, key=None):
		data = web.data()
		model = entity.__class__(**data)  #<3 python
		key = model.put()

		template = '%s_post' % entitiy.__name__

		data = {
				'key' : key
				}

		return getattr(render, template)(**data)

	@authorise
	def PUT(self, key=None):
		data = web.data()
		model = ndb.Key(urlsafe=key)

		for k in data.keys():
			setattr(model, k, data[k])

		key = model.put()

		template = '%s_put' % entity.__name__

		data = {
				'key' : key
			}

		return getattr(render, template)(**data)

	@authorise	
	def DELETE(self, key=None):
		k = ndb.Key(urlsafe=key)
		k.delete()

		return web.ok(200)

	
	def _json(self, model):
		dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None

		return json.dumps(model.to_dict(), default=dthandler)
		

class EntryController(Controller):
	'''Concrete handler for blog entries
	'''

	def __init__(self):
		Controller.__init__(self, Entry())

class CategoryController(Controller):
	'''Concrete handler for categories
	'''

	def __init(self):
		Controller.__init__(self, Category())
