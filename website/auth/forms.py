from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, EmailField, PasswordField, SubmitField, 
    BooleanField, SelectField, TextAreaField
)
from wtforms.validators import (
    DataRequired, Length, EqualTo, Email, ValidationError
)
from .models import User, Avatar

class RegisterForm(FlaskForm):
    username = StringField(u'Username', validators=[DataRequired(), Length(min=5)], render_kw={'placeholder': 'username'})
    password = PasswordField(u'Password', validators=[DataRequired(), Length(min=8, max=20)], render_kw={'placeholder': 'password'})
    email = EmailField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'email'})
    password2 = PasswordField('Password2', validators=[DataRequired(), EqualTo('password')], render_kw={'placeholder': 'repeat password'})
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different user name')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': 'username'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'password'})
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log in')

class NewProfilePicture(FlaskForm):
    name = StringField('Character name', validators=[DataRequired()], render_kw={'placeholder': 'character name'})
    url = StringField('Image link', validators=[DataRequired()], render_kw={'placeholder': 'paste link to image here'})
    rarity = SelectField('Rarity', choices=[4, 5])
    submit = SubmitField('Add new avatar to collection')

    def validate_name(self, name):
        avatar = Avatar.query.filter_by(name=name.data).first()
        if avatar is not None:
            raise ValidationError('This character is already exists')

class PostForm(FlaskForm):
    post = TextAreaField('Take inspiration and write something!', 
                        validators=[DataRequired(), Length(min=6, max=200)],
                        render_kw={'placeholder': 'here'})
    submit = SubmitField('Post')