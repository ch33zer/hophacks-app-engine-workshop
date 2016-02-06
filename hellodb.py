from google.appengine.ext import ndb

import webapp2

DEBUG = True

class HelloRecipient(ndb.Model):
    """Models someone who needs a hello"""
    hello_recipient = ndb.StringProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Hello, World!')
        # Find all.
        recipients = HelloRecipient.query()
        for recipient in recipients:
            self.response.write('<br />')
            self.response.write('<blockquote>Hello '+recipient.hello_recipient+'</blockquote>')
        self.response.out.write("""
          <form action="/hellodb/add_hello_recipient" method="post">
            <span><input type="text" name="recipient" rows="3" cols="60"></input></span>
            <span><input type="submit" value="Add Hello Recipient!"></span>
          </form>""")

class AddHello(webapp2.RequestHandler):
    def post(self):
        recipient_name = self.request.get('recipient')
        matching_recipients = HelloRecipient.query(HelloRecipient.hello_recipient==recipient_name)
        if matching_recipients.count():
            self.redirect('/hellodb')
            return
        recipient = HelloRecipient(hello_recipient=recipient_name)
        recipient.put()
        self.redirect('/hellodb')

app = webapp2.WSGIApplication([
    ('/.*/add_hello_recipient', AddHello),
    ('/.*', MainPage),
], debug=DEBUG)
