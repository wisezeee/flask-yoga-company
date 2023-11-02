from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField(gettext('Email', validators=[DataRequired()]))
    password = PasswordField(gettext('Password', validators=[DataRequired()]))
    password_submit = PasswordField(gettext('Password submit', validators=[DataRequired()]))
    name = StringField(gettext('Username', validators=[DataRequired()]))
    about = TextAreaField(gettext('About user'))
    submit = SubmitField(gettext('Submit'))
