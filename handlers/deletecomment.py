from handlers.postpage import PostPage
from models.post import Post
import time

class DeleteComment(PostPage):
    def post(self, post_id, comment_id):
        post = Post.by_id(post_id)
        creator = None
        comment = None
        if self.user and post:
            for c in post.comments:
                if c.key().id() == int(comment_id):
                    comment = c
            creator = post.comments.filter("created_by =", self.user.name).get()
        if creator and post and comment:
            comment.delete()
            time.sleep(0.1)
            self.redirect("/blog/%s" % (post_id))
        else:
            self.write("You're not the creator of this comment!")
