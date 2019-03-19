from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email

Gender_Pick = (('Male','Male'),('Female','Female'))

class UploadForm(FlaskForm):
    upload = FileField('Photo', validators=[ FileRequired(), FileAllowed(['png', 'PNG Images only!'])])
    description = StringField('Biography', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    location = StringField('Location', validators=[DataRequired()])
    userid = StringField('Username', validators=[DataRequired()])
    gender = SelectField(u'Gender', choices=Gender_Pick, validators=[DataRequired()])
