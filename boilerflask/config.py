#
# @author Cory Dolphin
# @wcdolphin
#
import os

class Config(object):
    """
    Basic default global configuration variables not specific to any environment
    """
    SQLALCHEMY_ECHO = False
    SOMECOOLCONSTANT = 3
    SECRET_KEY = 'verysecret'
    DEBUG = True



class DevelopmentConfig(Config):
    """ 
    The Development Configuration, provides default database and facebook credentials and
    configuration to run the application
    """ 
    SQLALCHEMY_DATABASE_URI = 'something local maybe?'
    FACEBOOK_APP_SECRET = "551e9288f0d937750251bbf98c1ab970"
    FACEBOOK_APP_ID = "440114152673475"
    CACHE_TYPE = 'simple'

class ProductionConfig(DevelopmentConfig):
    '''
    Extends and overrides declarations from the DevelopmentConfiguration
    '''
    FACEBOOK_APP_SECRET = "f2db0a7be3df73e89c069e98c9ab8ca9"
    FACEBOOK_APP_ID = "184933461628892"
    SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_ROSE_URL")


def getConfig():
    ''' Should return the proper configuration based upon environmental 
        variables and or other subsequent tests. Currently only distinguishes
        between Heroku and 'other', defaulting other to a local development database.
        TODO: test for local development database, if failed, default to a remote
        database, there should be no need for a full postgres install to test 
        or write client/HTML/CSS/js.
    '''
    if os.environ.get('PYTHONHOME') != None and 'heroku' in os.environ.get('PYTHONHOME'): ##we are on Heroku!
        return ProductionConfig
    else:
        return DevelopmentConfig
