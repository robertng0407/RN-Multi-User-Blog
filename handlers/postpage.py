from handlers.bloghandler import BlogHandler
from models.post import Post
from helpers import *
import time

class PostPage(BlogHandler):
    def get(self, post_id):
        # Grabs the post object based on post_id
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if post:
            post.comments.order('-created')

            # Verify if the logged in user is the same person who created the post
            if self.user:
                creator = self.user.name == post.created_by
            else:
                creator = None
            # Renders the post page. If creator is true, the page with show an update and delete button.
            # If creator is None, these buttons won't show
            self.render("post.html", p = post, creator = creator)

        else:
            self.error(404)
            return
