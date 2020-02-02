from flask_wtf import FlaskForm
from wtforms import Form, FieldList, FormField, IntegerField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class PersonForm(Form):

    username = StringField('Username', validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    restrictions = StringField("Dietary Restrictions", validators=[])
    isChef = BooleanField('Chef')
    mon = BooleanField("Monday")
    tues = BooleanField("Tuesday")
    wed = BooleanField("Wedesnesday")
    thurs = BooleanField("Thursday")
    fri = BooleanField("Friday")
    sat = BooleanField("Saturday")
    sun = BooleanField("Sunday")

class CreateGroupForm(FlaskForm):

    groupName = StringField("Group Name", validators=[])
    
    people = FieldList(
        FormField(PersonForm),
        min_entries=2,
        max_entries=10
    )
    submit = SubmitField('Create Group')
