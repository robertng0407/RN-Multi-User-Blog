from google.appengine.ext import db
from helpers import *

import hashlib

class User(db.Model):
    """User model for app store"""
    name = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

# Find user by id
    @classmethod
    def by_id(cls, uid):
        """Returns user by id"""
        return cls.get_by_id(uid, parent = users_key())

# Find user by name
    @classmethod
    def by_name(cls, name):
        """Returns user by name"""
        u = cls.all().filter('name =', name).get()
        return u

# Returns user model with passed in parameters
    @classmethod
    def register(cls, name, pw, email = None):
        """Returns User model"""
        pw_hash = make_pw_hash(name, pw)
        return cls(parent = users_key(),
                    name = name,
                    pw_hash = pw_hash,
                    email = email)

# Validates user and returns user object if true
    @classmethod
    def login(cls, name, pw):
        """Validates user and password is correct and returns user object"""
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u

# Delete all users
    @classmethod
    def delete_users(cls):
        """Delete all users"""
        all = cls.all()
        for user in all:
            user.delete()
