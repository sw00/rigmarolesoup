from google.appengine.ext import ndb

class Entry(ndb.Model):
	title = ndb.StringProperty(required=True)
	intro = ndb.StringProperty()
	content = ndb.TextProperty()
	timestamp = ndb.DateTimeProperty(auto_now_add=True)
	tags = ndb.StringProperty(repeated=True)
	published = ndb.BooleanProperty(required=True)


class Category(ndb.Model):
	name = ndb.StringProperty()
	desc = ndb.StringProperty(indexed=False)

