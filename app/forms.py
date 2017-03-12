from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class SignupForm(FlaskForm):
    firstname= StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    age = StringField('age', validators=[InputRequired()])
    bio = StringField('bio', validators=[InputRequired()])
    gender = StringField('gender', validators=[InputRequired()])
    