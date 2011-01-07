# -*- coding: utf-8 -*-

from bottle import Bottle, view, request
from google.appengine.api import xmpp
from settings import AUTHOR, EMAIL
from jidperson import JIDPerson, create_im

# Use a local object that can be imported from other modules as well
myapp = Bottle()

@myapp.get('/')
@view('index')
def index():
    """Index page.

    Shows only the subscription form.
    """
    return dict(author=AUTHOR, email=EMAIL)

@myapp.post('/')
@view('subscribe')
def subscribe():
    """Handle a subscription request.

    Save the Jabber ID only on successful invitation.
    """
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
    """View to list the subscribed JIDs.

    Admin only.
    """
    jids = [person.jid.address for person in JIDPerson.all()]
    return dict(author=AUTHOR, email=EMAIL, jids=jids)

@myapp.get('/post')
@view('post_message')
def show_post_form():
    """Show a form to post messages.

    Admin only.
    """
    return dict(author=AUTHOR, email=EMAIL, sent=False)

@myapp.post('/post')
@view('post_message')
def post_msg():
    """Handle new messages.

    Send the message to all subscribes JIDs.
    """
    jids = [person.jid.address for person in JIDPerson.all()]
    msg = request.forms.get('msg')
    for jid in jids:
        xmpp.send_message(jid, msg)
    return dict(author=AUTHOR, email=EMAIL, sent=True)

def invite_user(jid):
    """Send an XMPP invite to user."""
    res = xmpp.send_invite(jid)
    return True

def save_jid(jid):
    """Save JID only if it does not already exist."""
    query = JIDPerson.all()
    query.filter('jid =', create_im(jid))
    if not query.get():
        p = JIDPerson(jid=create_im(jid))
        p.put()
