from handlers.postpage import PostPage
from models.post import Post
from models.comment import Comment
import time

class DeleteComment(PostPage):
    def post(self, post_id, comment_id):
        post = Post.by_id(post_id)
        creator = None
        comment = Comment.by_id(comment_id)
        if self.user and post:
            creator = post.comments.filter("created_by =", self.user.name).get()
        if creator and post and comment:
            comment.delete()
            time.sleep(0.1)
            self.redirect("/blog/%s" % (post_id))
        else:
            self.write("You're not the creator of this comment!")
