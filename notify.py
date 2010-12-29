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
