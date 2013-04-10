#
# @author Cory Dolphin
# @wcdolphin
#

from flask import Flask, render_template, request, redirect, url_for, abort
#from flask.ext.sqlalchemy import SQLAlchemy #uncomment to use a relational database driver
#from flask.ext.mongoengine import MongoEngine #uncomment to use mongodb with mongoengine as a driver
#from flask.ext.login import (LoginManager,AnonymousUser) # want to handle login?
#from flask.ext.bcrypt import Bcrypt #want to hash passwords? (You should!)
#from flaskext.cache import Cache # want a cache?
import config #our super sweet configuration module!
from datetime import datetime
app = Flask(__name__)

__cfg = config.getConfig() #Are we running locally, in production? In Testing? This object will manage configuration!
app.config.from_object(__cfg) 
app.configType = __cfg

#db = SQLAlchemy(app) #uncomment for SQL database and ORM
#db = MongoEngine(app) #uncomment for Mongodb and ODM

#loginManager = LoginManager() #handle login and sessions
#crypt = Bcrypt(app) #bcrypt for password hashing
#cache = Cache(app)

#loginManager.setup_app(app)
#loginManager.login_view = "login"
#loginManager.login_message = u"Please log in to access this page."
#loginManager.refresh_view = "reauth"
#loginManager.session_protection = "strong"

print "Initialized with config:%s" % __cfg

from boilerflask import views