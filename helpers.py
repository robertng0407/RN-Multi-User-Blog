import jinja2
import os
import hmac
from google.appengine.ext import db
import re
import hashlib
import random
from string import letters

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

# Secret code to hmac
secret = 'Abklsu23kfj?asdk3ivn'

# Takes in template html file and pass in params
def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


# Takes in val parameter and returns string with val and hash
def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())


def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val



def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

def users_key(group = 'default'):
    return db.Key.from_path('users', group)


##### user stuff
# Creates salt for password hash
def make_salt(length = 5):
    return ''.join(random.choice(letters) for x in xrange(length))

# Pass in name, password and salt to create password hash
def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)

# Checks if password matches with hash, returns true if it does otherwise None
def valid_pw(name, password, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)

# Validates username input is correct
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

# Validates password input is correct
PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

# Validates email input is correct
EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)
