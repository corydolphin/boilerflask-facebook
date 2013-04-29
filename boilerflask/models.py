from boilerflask import app #db, cache, crypt # use a cache and a crypto library for users!
import datetime
import utils
import re

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