#
# @author Cory Dolphin
# @wcdolphin
#

from boilerflask import db, app
from boilerflask.models import User
from flask import flash
from flask.ext.wtf import (Form, TextField, Required, PasswordField, validators, FileField,
                                                    file_allowed, file_required)
#from flask.ext.login import current_user


'''
class LoginForm(Form):
    login_username = TextField(validators=[Required()])
    login_password = TextField(validators=[Required()])
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        self.rv = Form.validate(self)
        if not self.rv:
            return False
        tUser = User.getByUsername(self.login_username.data)
        if tUser ==None: #not a valid username
            tUser = User.getByEmail(self.login_username.data) #check if it is actaully an email address
            if tUser == None: 
                self.login_username.errors.append("The username you have entered does not exist")
                return False
            if tUser.is_oauth_user:
                self.login_username.errors.append("The email you have entered is associated with a Facebook account, please login using Facebook.")

        if not tUser.validatePassword(self.login_password.data):
            self.login_password.errors.append("It seems you have entered an incorrect password")
            return False

        self.user = tUser
        return True


class RegistrationForm(Form):
    reg_username = TextField('username', [validators.Required()])
    reg_email = TextField('Email Address', [validators.Required()])
    reg_password = PasswordField('password', [validators.Required(),validators.Length(min=4, max=100, message="Please enter a password longer than four characters")])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None
    
    def validate(self):
        rv = Form.validate(self)
        self.rv = rv

        usernameExists = User.query.filter(User.username== self.reg_username.data).count() != 0
        self.usernameExists = usernameExists
        if usernameExists:
            self.reg_username.errors.append('The username you have selected is already in use')
            return False

        emailExists = User.query.filter(User.email == self.reg_email.data).count() != 0
        self.emailExists = emailExists
        if emailExists:
            self.reg_email.errors.append('The email address you have selected is already in use!') #perhaps we should let users make multiple accounts?
            return False
        if self.rv:
            self.user = User(self.reg_email.data,self.reg_username.data, plainTextPassword = self.reg_password.data)
            db.session.add(self.user)
            db.session.commit()
        return self.rv
'''

