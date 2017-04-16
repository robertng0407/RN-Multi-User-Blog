from handlers.bloghandler import BlogHandler
from models.comment import Comment
from models.post import Post
import time



# Handles /comment route
class CommentHandler(BlogHandler):
    # Renders comment-form if user is logged in otherwise redirects to signup page
    def get(self, post_id):

        if Post.by_id(post_id) and self.user:
            self.render("comment-form.html", comment_page = "Post a Comment")
        else:
            self.redirect("/signup")


    def post(self, post_id):
        post = Post.by_id(post_id)
        if post and self.user:
            # Puts title, comment, and user into Gql
            title = self.request.get("title")
            comment = self.request.get("comment")
            if title and comment:
                make_comment = Comment.make_comment(post, self.user.name, comment, title)
                make_comment.put()
                time.sleep(0.1)

            # Gets the Post by id object, append the comment id, and puts into Gql

            # post.comment_id.append(make_comment.key().id())
            # post.put()

                self.redirect("/blog/%s" % (post_id))
            else:
                error = "Missing Fields!"
                self.render("comment-form.html", comment_page = "Post a Comment", error = error)
        else:
            self.redirect("/login")
