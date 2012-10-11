from google.appengine.ext import db

class Post(db.Model):
	title = db.StringProperty()
	body = db.TextProperty()
	created = db.DateTimeProperty(auto_now_add=True)

class Resource(db.Model):
	name = db.StringProperty()
	mimetype = db.StringProperty()
	uri = db.StringProperty()

class Category(db.Model):
	name = db.StringProperty()
	desc = db.StringProperty()

class Tags(db.Model):
	name = db.StringProperty()


