# -*- coding: utf-8 -*-

from google.appengine.ext import db


class JIDPerson(db.Model):
    jid = db.IMProperty(required=True, indexed=True)
    reg_date = db.DateProperty(auto_now_add=True)
        

def create_im(jid):
    return db.IM('xmpp', jid)
