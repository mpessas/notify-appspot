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

@myapp.get('/list')
@view('list_jids')
def list_jids():
    jids = [person.jid.address for person in JIDPerson.all()]
    return dict(author=AUTHOR, email=EMAIL, jids=jids)

@myapp.get('/post')
@view('post_message')
def show_post_form():
    return dict(author=AUTHOR, email=EMAIL, sent=False)

@myapp.post('/post')
@view('post_message')
def post_msg():
    jids = [person.jid.address for person in JIDPerson.all()]
    msg = request.forms.get('msg')
    for jid in jids:
        xmpp.send_message(jid, msg)
    return dict(author=AUTHOR, email=EMAIL, sent=True)

def invite_user(jid):
    res = xmpp.send_invite(jid)
    return True

def save_jid(jid):
    query = JIDPerson.all()
    query.filter('jid =', create_im(jid))
    if not query.get():
        p = JIDPerson(jid=create_im(jid))
        p.put()
