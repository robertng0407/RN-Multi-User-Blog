from handlers.bloghandler import BlogHandler
from models.post import Post
from helpers import *

class NewPost(BlogHandler):
    def get(self):
        # If user is logged in, newpost page will render otherwise redirects to login page
        if self.user:
            self.render("newpost.html", post_page = "New Post")
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            self.redirect('/login')
            return

        subject = self.request.get('subject')
        content = self.request.get('content')

        # If user enters subject and content, put data into database and redirects to blog post
        if subject and content:
            user = self.user
            p = Post(user = user ,parent = blog_key(), subject = subject, content = content, created_by = self.user.name)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))

        # Otherwiser, error will appear
        else:
            error = "Subject and content missing!"
            self.render("newpost.html", post_page = "New Post",subject=subject, content=content, error=error)
