from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    first_name = StringField('Firstname', validators=[InputRequired()])
    last_name = StringField('Lastname', validators=[InputRequired()])
    id = StringField('Id', validators=[InputRequired()])