from handlers.postpage import PostPage
from models.post import Post

class LikePost(PostPage):
    def post(self, post_id):
        post = Post.by_id(post_id)

        if self.user and post:
            creator = self.user.name == post.created_by
            if creator:
            # If creator of post is the same as logged in user, an error will render on page
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
