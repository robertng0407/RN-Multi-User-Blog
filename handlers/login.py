from handlers.bloghandler import BlogHandler
from models.user import User

class Login(BlogHandler):
    # If user already logged in, redirects to blog otherwise renders login form
    def get(self):
        if self.user:
            self.redirect("/blog")
        else:
            self.render('login-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/blog')
        else:
            msg = 'Invalid login'
            self.render('login-form.html', error = msg)
