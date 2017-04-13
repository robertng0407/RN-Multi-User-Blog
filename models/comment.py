from google.appengine.ext import db
from models.post import Post

# Comment model for app store
class Comment(db.Model):
    post = db.ReferenceProperty(Post, collection_name = "comments")

    created_by= db.StringProperty(required = True)
    comment = db.TextProperty(required = True)
    title = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

# Returns comment object by id
    @classmethod
    def by_id(cls, id):
        return cls.get_by_id(int(id))

# Returns Comment model with passed in parameters
    @classmethod
    def make_comment(cls, post, created_by, comment, title):
        return cls(post = post,
                   created_by = created_by,
                   comment = comment,
                   title = title)

# Delete all comments
    @classmethod
    def delete_comments(cls):
        all = cls.all()
        for comment in all:
            comment.delete()
