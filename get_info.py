# The forms for getting new information to add to the database. 
# Validators ensure that everythings filled out and no one puts the entirety of the bee movie script in a field.

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ArtInputForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    artist = StringField('Artist', validators=[DataRequired(), Length(max=50)]])
    price = DecimalField('Price', validators=[DataRequired()])

    submit=SubmitField('Add Artwork')

class ArtistInputForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    email_address = StringField('Email', validators=[DataRequired(), Email(),  Length(max=50)]])

    submit=SubmitField('Add Artist')