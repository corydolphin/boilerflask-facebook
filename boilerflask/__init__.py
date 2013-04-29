from flask import Flask, render_template, request, redirect, url_for, abort
import config #our super sweet configuration module!
from datetime import datetime
from flask.ext.mongoengine import MongoEngine
from flask_oauth import OAuth

app = Flask(__name__)

__cfg = config.getConfig() #Are we running locally, in production? In Testing? This object will manage configuration!
app.config.from_object(__cfg) 
app.configType = __cfg




db = MongoEngine(app) #database and ORM
oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=app.config['FACEBOOK_APP_ID'],
    consumer_secret=app.config['FACEBOOK_APP_SECRET'],
    request_token_params={'scope': 'email,manage_notifications'}
)


print "Initialized with config:%s" % __cfg

from boilerflask import views