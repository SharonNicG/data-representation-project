# Reference 
    # https://www.oreilly.com/library/view/flask-web-development/9781491947586/ch04.html
    # https://pythonspot.com/flask-web-forms/
    # https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
    # https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
