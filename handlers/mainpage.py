from handlers.bloghandler import BlogHandler

# Redirects to /blog when visiting / route
class MainPage(BlogHandler):
  def get(self):
      self.redirect("/blog")
