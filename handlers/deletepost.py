from handlers.postpage import PostPage
from models.post import Post
import time

# Delete post handler
class DeletePost(PostPage):
    def post(self, post_id):
        if post_id:
            post = Post.by_id(post_id)
        else:
            self.error(404)
            return

        if self.user and post:
            creator = self.user.name == post.created_by or None
            if creator:
                post.delete()
                time.sleep(0.1)
                self.redirect("/")
            else:
                self.write("You are not the author of this post!")
        else:
            self.redirect("/login")
