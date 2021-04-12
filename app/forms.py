from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired



class UploadForm (FlaskForm):
    description = StringField('Description', widget=TextArea(), validators=[DataRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
