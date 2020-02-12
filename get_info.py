from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ArtInputForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    artist = StringField('Artist', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])

    submit=SubmitField('Add Artwork')

class ArtistInputForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    email_address = StringField('Email', validators=[DataRequired(), Email()])

    submit=SubmitField('Add Artist')