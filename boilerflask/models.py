#
# @author Cory Dolphin
# @wcdolphin
#

from boilerflask import app #db, cache, crypt # use a cache and a crypto library for users!
import datetime
import utils
import re

""" Uncomment for user model with sqlalchemy
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
"""

""" Uncomment for user model
class User(db.Document):
    email = db.StringField(required=False)
    username = db.StringField(required=True)
    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def __unicode(self):
        return u'user:{"username":%s, "email":%s}' % (self.username, self.email)
"""