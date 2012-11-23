#
# @author Cory Dolphin
# @wcdolphin
#

from boilerflask import db, app #, cache, crypt # use a cache and a crypto library for users!
import datetime
import utils
import re
import facebook

class User(db.Model):
    '''
    This object represents a registered user
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40))
    username = db.Column(db.String(40))

    def __init__(self, email, username):
        self.email = email
        self.username = username

    def __repr__(self):
        return '{User %r}' % self.username