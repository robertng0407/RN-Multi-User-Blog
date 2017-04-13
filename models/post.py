from google.appengine.ext import db
from models.comment import Comment
from helpers import *
from models.user import User

# Post model for app store
class Post(db.Model):

    # Reference to User model (One to many)
    user = db.ReferenceProperty(User, collection_name = "user_posts")

    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    created_by = db.StringProperty(required = True)
    votes = db.IntegerProperty()
    user_who_voted = db.ListProperty(str)
    comment_id = db.ListProperty(int)
    last_modified = db.DateTimeProperty(auto_now = True)

# Replaces new lines with a break
    def render_text(self):
        self._render_text = self.content.replace('\n', '<br>')
        return self._render_text

# Returns comment object from Comment model based on id from comment_id
    def render_comment(self, id):
        comment = Comment.by_id(id)
        return comment

# Deletes all posts
    @classmethod
    def delete_post(cls):
        all = cls.all()
        for post in all:
            post.delete()

# Returns Post object based on id
    @classmethod
    def by_id(cls, post_id):
        return cls.get_by_id(int(post_id), parent = blog_key())

# Returns length of users who voted
    @property
    def likes(self):
        return len(self.user_who_voted)
