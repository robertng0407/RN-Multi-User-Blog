from handlers.bloghandler import BlogHandler

class Welcome(BlogHandler):
    def get(self):
        # If user already logged in, renders welcome page with username otherwise redirects to signup page
        if self.user:
            self.render('welcome.html', username = self.user.name)
        else:
            self.redirect('/signup')
