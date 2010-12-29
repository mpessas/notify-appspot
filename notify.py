# -*- coding: utf-8 -*-

from bottle import Bottle, view
from google.appengine.api import users
from settings import AUTHOR, EMAIL

myapp = Bottle()

@myapp.route('/')
@myapp.route('/index.html')
@view('index')
def index():
    return dict(author=AUTHOR, email=EMAIL)

@myapp.route('/login')
def login():
    user = users.get_current_user()
    if user:
        return "<p>Hi %s</p>" % user.nickname()
    else:
        return "<p>Hi, anonymous</p>"
