from flask-wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.valitdators import DataRequired, Length, Email

class CreateGroupForm(FlaskForm):
    username = StringField('Username,' validators=[DataRequired(), Length(min=3, max)=15])
    email = StringField('Email', validators=[DataRequired(), Email()])

    submit = SubmitField('Create Group')