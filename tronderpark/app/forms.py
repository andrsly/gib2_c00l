from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import user1

class LoginForm(FlaskForm):
    username = StringField('Brukernavn', validators=[DataRequired()])
    password = PasswordField('Passord', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Logg inn')

class RegistrationForm(FlaskForm):
    username = StringField('Brukernavn', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Passord', validators=[DataRequired()])
    password2 = PasswordField(
        'Gjenta passord', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrer')

    def validate_username(self, username):
        user = user1.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Vennligst bruk et annet brukernavn.')

    def validate_email(self, email):
        user = user1.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Vennligst bruk en annen email.')