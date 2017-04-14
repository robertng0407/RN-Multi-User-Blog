from handlers.bloghandler import BlogHandler
from models.post import Post
from helpers import *
import time

class PostPage(BlogHandler):
    def get(self, post_id):
        # Grabs the post object based on post_id
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        post.comments.order('-created')

        # Verify if the logged in user is the same person who created the post
        creator = self.user.name == post.created_by or None

        if not post:
            self.error(404)
            return

        # Renders the post page. If creator is true, the page with show an update and delete button.
        # If creator is None, these buttons won't show
        self.render("post.html", p = post, creator = creator)
    def post(self, post_id):
        post = Post.by_id(post_id)
        creator = self.user.name == post.created_by or None
        # Delete post if user clicks delete
        delete = self.request.get("delete")
        if delete == "delete":
            post.delete()
            time.sleep(0.1)
            self.redirect("/")

        # Upvote/Downvote
        else:
            if self.user:
                post = Post.by_id(post_id)
                # If creator of post is the same as logged in user, an error will render on page
                if self.user.name == post.created_by:
                    error_vote = "You can't vote on your own post!"
                    self.render("post.html", p = post, creator = creator, error_vote = error_vote)
                else:
                    # vote = int(self.request.get("vote"))
                    # If logged in user is not post creator, user can upvote/downvote
                    if self.user.name not in post.user_who_voted:
                        # Appends to user_who_voted list in Post model to keep track of who voted
                        post.user_who_voted.append(self.user.name)
                        post.put()
                        self.redirect("/blog/%s" % (post_id))
                    else:
                        # If user already voted, an error will appear
                        error_vote = "You've already voted!"
                        self.render("post.html", p = post, creator = creator, error_vote = error_vote)
            else:
                self.redirect("/login")
