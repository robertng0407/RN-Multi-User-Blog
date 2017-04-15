from handlers.bloghandler import BlogHandler
from models.post import Post

class UpdatePost(BlogHandler):
    def get(self, blog_id):
        post = Post.by_id(blog_id)
        # Only post creator will be update blog post otherwise, it will redirect to login page.
        if self.user and post:
            if self.user.name == post.created_by:
                self.render("newpost.html", post_page = "Update Post", subject = post.subject, content = post.content, blog_id = post.key().id())
            else:
                self.redirect("/login")
        else:
            self.error(404)
            return

    # Updates Qgl with new subject and content
    def post(self, blog_id):
        post = Post.by_id(blog_id)
        subject = self.request.get("subject")
        content = self.request.get("content")
        if self.user and post:
            if self.user.name == post.created_by:
                if subject and content:
                    post.subject = subject
                    post.content = content
                    post.put()
                    print post.created_by

                    self.redirect("/blog/%s" % (blog_id))
                else:
                    error = "Subject and content missing!"
                    self.render("newpost.html", post_page = "New Post", subject=subject, content=content, error=error, blog_id = post.key().id())
        else:
            self.error(404)
            return
