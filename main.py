#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
from helpers import *

# Models
from models.user import User
from models.post import Post
from models.comment import Comment

# Handlers
from handlers.bloghandler import BlogHandler
from handlers.signup import Signup
from handlers.register import Register
from handlers.welcome import Welcome
from handlers.logout import Logout
from handlers.login import Login
from handlers.comment import CommentHandler
from handlers.mainpage import MainPage
from handlers.blogfront import BlogFront
from handlers.postpage import PostPage
from handlers.updatepost import UpdatePost
from handlers.newpost import NewPost
from handlers.deletepost import DeletePost
from handlers.likepost import LikePost
from handlers.updatecomment import UpdateComment


# Routes
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/blog/?', BlogFront),
                               ('/blog/(\d+)', PostPage),
                               ('/blog/(\d+)/comment', CommentHandler),
                               ('/blog/(\d+)/update', UpdatePost),
                               ('/blog/(\d+)/delete', DeletePost),
                               ('/blog/(\d+)/like', LikePost),
                               ('/blog/(\d+)/comment/(\d+)', UpdateComment),
                               ('/blog/newpost', NewPost),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/welcome', Welcome),
                               ],
                              debug=True)
