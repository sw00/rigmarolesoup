from google.appengine.ext import ndb

class Post(ndb.Model):
	title = ndb.StringProperty()
	body = ndb.TextProperty()
	created = ndb.DateTimeProperty(auto_now_add=True)
	category = ndb.KeyProperty()
	tags = ndb.KeyProperty(repeated=True)

	@classmethod
	def fetch_all(cls, *filters):
		return cls.query(*filters).order(cls.created)

class Category(ndb.Model):
	name = ndb.StringProperty()
	desc = ndb.StringProperty(indexed=False)


class Tag(ndb.Model):
	name = ndb.StringProperty()

