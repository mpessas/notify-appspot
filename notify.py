# -*- coding: utf-8 -*-

from bottle import Bottle, view, request
from google.appengine.api import users
from settings import AUTHOR, EMAIL

myapp = Bottle()

@myapp.get('/')
@view('index')
def index():
    return dict(author=AUTHOR, email=EMAIL)

@myapp.post('/subscription')
@view('subscribe')
def subscribe():
    name = request.forms.get('email')
    return dict(author=AUTHOR, email=EMAIL, res='success')
