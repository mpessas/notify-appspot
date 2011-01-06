# -*- coding: utf-8 -*-

from bottle import Bottle, view, request
from google.appengine.api import xmpp
from settings import AUTHOR, EMAIL
from jidperson import JIDPerson, create_im

import bottle
bottle.debug(True)

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
            save_jid(jid)
            return dict(author=AUTHOR, email=EMAIL, res=True)
        else:
            return dict(author=AUTHOR, email=EMAIL, res=False)
    except xmpp.Error, e:
        return dict(author=AUTHOR, email=EMAIL, res=False)

def invite_user(jid):
    res = xmpp.send_invite(jid)
    return True

def save_jid(jid):
    p = JIDPerson(jid=create_im(jid))
    p.put()
