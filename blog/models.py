from google.appengine.ext import ndb

class Entry(ndb.Model):
	title = ndb.StringProperty(required=True)
	alias = ndb.StringProperty(required=True)
	intro = ndb.StringProperty(required=True)
	content = ndb.TextProperty()
	timestamp = ndb.DateTimeProperty(auto_now_add=True)
	tags = ndb.StringProperty(repeated=True)
	published = ndb.BooleanProperty(required=True)
	category = ndb.KeyProperty(required=True)


class Category(ndb.Model):
	name = ndb.StringProperty()
	desc = ndb.StringProperty(indexed=False)

class Image(ndb.Model):
	parent_entry = ndb.KeyProperty()
	title = ndb.StringProperty()
	caption = ndb.StringProperty()
	blobkey = ndb.BlobKeyProperty()

