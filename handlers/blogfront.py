from handlers.bloghandler import BlogHandler
from models.post import Post

class BlogFront(BlogHandler):
    # Renders the blog page with all posts

    def get(self):
        posts = greetings = Post.all().order('-created')
        self.render('front.html', posts = posts)
