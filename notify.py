# -*- coding: utf-8 -*-

from bottle import Bottle, view
from google.appengine.api import users
from settings import AUTHOR, EMAIL

myapp = Bottle()

@myapp.get('/')
@view('index')
def index():
    return dict(author=AUTHOR, email=EMAIL)

@myapp.post('/')
def subscribe():
    name = myapp.request.forms.get('email')
    return '{"res": "success"}'
