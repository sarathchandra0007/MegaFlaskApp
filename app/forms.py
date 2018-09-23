from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User

class LoginForm(FlaskForm):
    username    = StringField('Username',validators=[DataRequired()])
    password    = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit      = SubmitField('Sign In')

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
