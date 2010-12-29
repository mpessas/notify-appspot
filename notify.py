# -*- coding: utf-8 -*-

from bottle import Bottle, view, request
from google.appengine.api import xmpp
from settings import AUTHOR, EMAIL

myapp = Bottle()

@myapp.get('/')
@view('index')
def index():
    return dict(author=AUTHOR, email=EMAIL)

@myapp.post('/')
@view('subscribe')
def subscribe():
    jid = request.forms.get('jid')
    try:
        if invite_user(jid):
            return dict(author=AUTHOR, email=EMAIL, res=True)
        else:
            return dict(author=AUTHOR, email=EMAIL, res=False)
    except xmpp.Error, e:
        return dict(author=AUTHOR, email=EMAIL, res=False)

def invite_user(jid):
    res = xmpp.send_invite(jid)
    return True
