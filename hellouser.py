from google.appengine.api import users
import webapp2

DEBUG = True

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        if user:
            self.response.write('Hello, ' + user.nickname())
            self.response.write('<br />')
            self.response.write('Your username is: ' + user.email())
            self.response.write('<br />')
            self.response.write('Your globally unique ID is: ' + user.user_id())
            self.response.write('<br />')
            self.response.write('<a href="'+users.create_logout_url('/hellouser')+'">log out</a>')
        else:
            self.response.write('Hello, nobody')
            self.response.write('<br />')
            self.response.write('<a href="'+users.create_login_url('/hellouser')+'">log in</a>')

app = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=DEBUG)
