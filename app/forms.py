from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User
from flask_babel import _, lazy_gettext as _l

class LoginForm(FlaskForm):
    username    = StringField(_l('Username'),validators=[DataRequired()])
    password    = PasswordField(_l('Password'),validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))
    submit      = SubmitField(_l('Sign In'))

class RegistrationForm(FlaskForm):
    username    = StringField('Username',validators=[DataRequired()])
    email       = StringField('Email',validators=[DataRequired(), Email()])
    password    = PasswordField('Password',validators=[DataRequired()])
    password2   = PasswordField('Re-enter Password', validators=[DataRequired(), EqualTo('password')])
    submit      = SubmitField('Sign In')

    # custom validators

    def validate_username(self,username):
        user    = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError('Username entered exists, enter another name')
    def validate_email(self,email):
        email   = User.query.filter_by(email = email.data).first()
        if email is not None:
            raise ValidationError('Email entered exists, enter another email')

class EditProfileForm(FlaskForm):
    username    = StringField('Username',validators=[DataRequired()])
    about_me    = TextAreaField('About me',validators=[Length(min=0,max=140)])
    submit      = SubmitField('Submit')

    def __init__(self,original_username,*args,**kwargs): #If we are updating with same userbane
        super(EditProfileForm,self).__init__(*args,**kwargs)
        self.original_username=original_username

    def validate_username(self,username):
        if username.data != self.original_username:
            user    = User.query.filter_by(username = username.data).first()
            if user is not None:
                raise ValidationError('Username entered exists, enter another name')


class Postform(FlaskForm):
    post = TextAreaField('Post Something',validators=[DataRequired(),Length(min=1,max=140)])
    submit = SubmitField('Submit')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Request for password reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
