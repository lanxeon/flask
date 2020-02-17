from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SearchBar(FlaskForm):
	search=StringField('Search', validators=[DataRequired(),Length(min=2,max=15)])