# -*- coding: utf-8 -*-

from google.appengine.ext import db


class JIDPerson(db.Model):
    """Model for the subscribers."""
    jid = db.IMProperty(required=True, indexed=True)
    reg_date = db.DateProperty(auto_now_add=True)
        

def create_im(jid):
    """Function to allow creation of IM objects from JIDs."""
    return db.IM('xmpp', jid)
