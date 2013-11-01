from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required, ValidationError

def fisk(form, field):
    if not len(field.data) >= 2:
        raise ValidationError("Bla bla test (len=%s)" % len(field.data))

class LoginForm(Form):
    username = TextField('username', validators=[Required(), fisk])
    password = TextField('password', validators=[Required(), fisk])
    remember_me = BooleanField('remember_me', default=False)