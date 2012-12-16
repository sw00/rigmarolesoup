import webapp2
import urllib

from webapp2_extras import mako

from models import Resource
from google.appengine.ext import ndb, blobstore
from google.appengine.ext.webapp import blobstore_handlers

class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def mako(self):
        # Returns a Mako renderer cached in the app registry.
        return mako.get_mako(app=self.app)

    def render_response(self, _template, **context):
        # Renders a template and writes the result to the response.
        rv = self.mako.render_template(_template, **context)
        self.response.write(rv)

class MainHandler(BaseHandler):
	def get(self):
		""" Return the upload form
		"""
	#	q = Resource.query()
	#	images = q.filter(Resource.parent==ndb.Key(urlsafe=parent_key)).fetch()
		
#		parent_key = self.request.get('parent')

		upload_url = blobstore.create_upload_url('/blob/upload')
		self.render_response('upload.html',upload_url=upload_url)


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):
		""" Do the actual upload
		"""
		upload_files = self.get_uploads('file')
		print len(upload_files)
		blob_info = upload_files[0]

		#parent_key = urllib.unquote(self.request.get('parent'))
		
		resource = Resource(
				title = blob_info.filename,
				parent = None,
				caption = '',
				blobkey = blob_info.key()
				) 

		resource.put()

		self.redirect('/serve/%s' % blob_info.key())

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
	def get(self, resource):
		resource = resource
		blob_info = blobstore.BlobInfo.get(resource)
		self.send_blob(blob_info)

app = webapp2.WSGIApplication([(r'/blob/uploadForm', MainHandler),
								(r'/blob/upload', UploadHandler),
								(r'/serve/([^/]+)?', ServeHandler)],
								debug=True)


