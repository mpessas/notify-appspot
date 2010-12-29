# -*- coding: utf-8 -*-

import bottle
from google.appengine.ext.webapp import util
from notify import myapp

util.run_wsgi_app(myapp)
