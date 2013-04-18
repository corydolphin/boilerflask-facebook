from flask import Flask, render_template, request
#from boilerflask.models import User
#from boilerflask.forms import (LoginForm)
from boilerflask import app #, loginManager, crypt, db, cache
import utils
import facebook

@app.route('/', methods=['GET'] )
def index():
    user = getFacebookUser()
    facebook_profile = None
    notifications = None
    if user:

        graph = facebook.GraphAPI(user["access_token"])
        facebook_profile = graph.get_object("me")
        notifications = graph.get_object("me/notifications")

    print "User:%s" % user
    print "Profile:%s" % facebook_profile
    print "Notifications:%s" % notifications

    return render_template('index.html', facebook_profile=facebook_profile, notifications=notifications)

@app.route('/notifier', methods=['GET'] )
def notifier():
    user = getFacebookUser()
    facebook_profile = None
    notifications = None
    # check notifications
    # decide to send notifications
    # blahahaha
    if user:
        graph = facebook.GraphAPI(user["access_token"])
        facebook_profile = graph.get_object("me")
        notifications = graph.get_object("me/notifications")

    print "User:%s" % user
    print "Profile:%s" % facebook_profile
    print "Notifications:%s" % notifications
    return "foo"

def getFacebookUser():
    user = facebook.get_user_from_cookie(request.cookies, app.config['FACEBOOK_APP_ID'], app.config['FACEBOOK_APP_SECRET'])
    return user

@app.errorhandler(404)
def page_not_found(error):
    return 'Cory should really handle this page_not_found'


@app.errorhandler(403)
def forbidden(error):
    return 'Cory should really handle this forbidden'


@app.errorhandler(500)
def internal_server_error(error):
    return 'Cory should really handle this internal server error'

