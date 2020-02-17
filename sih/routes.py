from flask import render_template, url_for, request, redirect, flash
from sih import app,db,lm,bcrypt
from sih.forms import reg,log,regDetails
from sih.models import User


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')



@app.route('/register', methods=['GET','POST'])
def register():
	form=reg()
	if form.validate_on_submit():
		flash(f'Registered Successfully')
		return redirect(url_for('medhistory'))
	else:
		print(form.errors)

	return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
	form=log()

	if form.validate_on_submit():
		flash(f'Welcome {form.email.data}')
		

@app.route('/medhistory', methods=['POST', 'GET'])
def medhistory():
	form=regDetails()
	
	if form.validate_on_submit():
		print(form.bgrp.data)
	else:
		print(form.errors)
	return render_template('medreg.html', form=form)