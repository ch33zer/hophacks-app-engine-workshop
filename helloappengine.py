import webapp2

DEBUG = True

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Hello, World!')

app = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=DEBUG)
