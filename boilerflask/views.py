from flask import Flask, render_template, request, session, redirect, url_for
from boilerflask import app, facebook
from facebook_helper import *
from boilerflask.models import User

@app.route('/', methods=['GET'] )
def index():
    if not 'oauth_token' in session:
        return redirect(url_for('login'))
    else:

        facebook_profile = facebook.get('/me')

        if facebook_profile.status == 200: #200 means success
            facebook_profile =  facebook_profile.data
            print facebook_profile['name']
            print facebook_profile['id']
            print session.get('oauth_token')[0]
            user = User.objects(facebook_id=facebook_profile['id']).first()
            if not user:
                user = User(facebook_id=facebook_profile['id'], access_token=session.get('oauth_token')[0], name=facebook_profile['name'])
            else:
                user.oauth_token = session.get('oauth_token')
            
            print user.save()
            print "succesfully saved user hopefully"
        else:
            print "get facebook/me failed"


        notifications = facebook.get("me/notifications")
        
        if notifications.status == 200: #200 means success
            notifications =  notifications.data
        else:
            print "get facebook/me/notifications failed"

    print "Profile:%s" % facebook_profile
    print "Notifications:%s" % notifications

    return render_template('index.html', facebook_profile=facebook_profile, notifications=notifications)

@app.route('/notifier', methods=['GET'] )
def notifier():
    if not 'oauth_token' in session:
        return redirect(url_for('login'))
    notifications = facebook.get("me/notifications")
    
    if notifications.status == 200: #200 means success
        notifications =  notifications.data
    else:
        print "get facebook/me/notifications failed"

    return '%s' % notifications


