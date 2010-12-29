# -*- coding: utf-8 -*-

from bottle import route, run, Bottle
from google.appengine.api import users

myapp = Bottle()

@myapp.route('/')
@myapp.route('/index.html')
def index():
    return "<a href='/login'>Log in</a>"

@myapp.route('/login')
def login():
    user = users.get_current_user()
    if user:
        return "<p>Hi %s</p>" % user.nickname()
    else:
        return "<p>Hi, anonymous</p>"
