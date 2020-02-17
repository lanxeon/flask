from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,RadioField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from sih.models import User

class reg(FlaskForm):
	usn=StringField('Username', validators=[DataRequired(), Length(min=3,max=15)])
	email=StringField('Email', validators=[DataRequired(), Email()])
	pwd=PasswordField('Password', validators=[DataRequired(), Length(min=5,max=15)])
	repwd=PasswordField('Confirm Password', validators=[DataRequired(), Length(min=5,max=15),EqualTo('pwd')])
	submit=SubmitField('Register')

	def validate_email(self, email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			return ValidationError('Already registered with the specified email')

	def validate_usn(self, usn):
		user=User.query.filter_by(usn=usn.data).first()
		if user:
			return ValidationError('Username already taken. Please choose another one')


class log(FlaskForm):
	email=StringField('Email', validators=[DataRequired(), Email()])
	pwd=PasswordField('Password', validators=[DataRequired(), Length(min=5,max=15)])
	rememberme=BooleanField('Remember me')
	submit=SubmitField('Log in')

class regDetails(FlaskForm):
	bgrp=SelectField('Enter blood group', choices=[('A+','A+'),('A-','A-'),('B+','B+'), ('B-','B-'),('AB+','AB+'),('AB-','AB-'),
																	('O+','O+'),('O-','O-')])
	disease1=StringField('Enter 1st Disease')
	disease2=StringField('Enter 2nd Disease')
	disease3=StringField('Enter 3rd Disease')
	disease4=StringField('Enter 4th Disease')
	disease5=StringField('Enter 5th Disease')
	submit=SubmitField('Enter')