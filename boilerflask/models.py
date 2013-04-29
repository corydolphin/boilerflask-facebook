from boilerflask import app, db
import datetime
import utils
import re


class User(db.Document):
    facebook_id = db.StringField(required=True)
    access_token = db.StringField(required=True)
    name = db.StringField(required=True)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u'User:{"name":%s, facebook_id":%s, "access_token":%s}' % (self.name, self.facebook_id, self.access_token)