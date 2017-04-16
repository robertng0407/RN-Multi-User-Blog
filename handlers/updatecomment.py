from handlers.postpage import PostPage
from models.post import Post
from models.comment import Comment
import time

class UpdateComment(PostPage):
    def get(self, post_id, comment_id):
        post = Post.by_id(post_id)
        creator = None
        comment = Comment.by_id(comment_id)
        if self.user and post:
            creator = post.comments.filter("created_by =", self.user.name).get()
        if creator and post and comment:
            self.render("comment-form.html", comment_page = "Update comment", comment = comment.comment, title = comment.title)
        else:
            self.error(404)
            return
    def post(self, post_id, comment_id):
        post = Post.by_id(post_id)
        creator = None
        comment_obj = Comment.by_id(comment_id)
        if self.user and post:
            creator = self.user.name == comment_obj.created_by
        if creator and post and comment_obj:
            title = self.request.get("title")
            comment = self.request.get("comment")
            comment_obj.title = title
            comment_obj.comment = comment
            comment_obj.put()
            time.sleep(0.1)
            self.redirect("/blog/%s" % (post_id))
        else:
            self.redirect("/login")
