# -*- coding: utf-8 -*-

import  bottle
from google.appengine.ext.webapp import util

util.run_wsgi_app(bottle.default_app())
