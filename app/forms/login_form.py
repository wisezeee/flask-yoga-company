from flask_babel import gettext

from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField(gettext('Email', validators=[DataRequired()]))
    password = PasswordField(gettext('Password', validators=[DataRequired]))
    remember_me = BooleanField(gettext('Remember'))
    submit = SubmitField(gettext('Login'))
