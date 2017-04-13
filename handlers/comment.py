from handlers.bloghandler import BlogHandler
from models.comment import Comment
from models.post import Post



# Handles /comment route
class CommentHandler(BlogHandler):
    # Renders comment-form if user is logged in otherwise redirects to signup page
    def get(self, post_id):
        if self.user:
            self.render("comment-form.html")
        else:
            self.redirect("/signup")


    def post(self, post_id):
        if self.user:
            # Puts title, comment, and user into Gql
            title = self.request.get("title")
            comment = self.request.get("comment")
            make_comment = Comment.make_comment(self.user.name, comment, title)
            make_comment.put()

            # Gets the Post by id object, append the comment id, and puts into Gql
            post = Post.by_id(post_id)
            post.comment_id.append(make_comment.key().id())
            post.put()

            self.redirect("/blog/%s" % (post_id))
