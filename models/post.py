from google.appengine.ext import db
# from models.comment import Comment
from helpers import *
from models.user import User

# Post model for app store
class Post(db.Model):
    """Post model for app store"""
    # Reference to User model (One to many)
    user = db.ReferenceProperty(User, collection_name = "user_posts")

    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    created_by = db.StringProperty(required = True)
    votes = db.IntegerProperty()
    user_who_voted = db.ListProperty(str)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render_text(self):
        """Replaces new lines with a break"""
        self._render_text = self.content.replace('\n', '<br>')
        return self._render_text

    @classmethod
    def delete_post(cls):
        """Delete all posts"""
        all = cls.all()
        for post in all:
            post.delete()

    @classmethod
    def by_id(cls, post_id):
        """Returns post by id"""
        return cls.get_by_id(int(post_id), parent = blog_key())

    @property
    def likes(self):
        """Returns length of users who voted"""
        return len(self.user_who_voted)
