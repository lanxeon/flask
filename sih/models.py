from sih import db, lm
from flask_login import UserMixin


@lm.user_loader
def load_user(userid):
	return User.query.get(int(userid))

class User(db.Model, UserMixin):
	id=db.Column(db.Integer,nullable=False,primary_key=True, autoincrement=True)
	usn=db.Column(db.String(20),unique=True,nullable=False)
	email=db.Column(db.String(20),unique=True, nullable=False)
	password=db.Column(db.String(60),nullable=False)
	bgrp=db.Column(db.String(3),nullable=False)
	d1=db.Column(db.String(30))
	d2=db.Column(db.String(30))
	d3=db.Column(db.String(30))
	d4=db.Column(db.String(30))
	d5=db.Column(db.String(30))

	def __repr__(self):
		return f"User('{self.usn}' , '{ self.email }')"


