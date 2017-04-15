from handlers.postpage import PostPage
from models.post import Post
import time

# Delete post handler
class DeletePost(PostPage):
    def post(self, post_id):
        post = Post.by_id(post_id)
        if self.user:
            creator = self.user.name == post.created_by
        else:
            creator = None

        if self.user and post:
            if creator:
                post.delete()
                time.sleep(0.1)
                self.redirect("/")
        else:
            self.redirect("/login")
