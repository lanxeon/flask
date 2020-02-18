from flask import render_template, url_for, request, redirect, flash
from unisys import app, lm, bcrypt, db, socketio
from flask_socketio import send, emit
import os
from unisys.forms import Registration, Login
from unisys.models import User


@app.route('/')
@app.route('/home')
def home():
	full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'unisys_logo.jpg')
	full_filename1 = os.path.join(app.config['UPLOAD_FOLDER'], 'abstract2.jpg')
	full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'capacity.jpg')
	full_filename3 = os.path.join(app.config['UPLOAD_FOLDER'], 'cover1.jpg')
	full_filename4 = os.path.join(app.config['UPLOAD_FOLDER'], 'pp1.png')
	full_filename5 = os.path.join(app.config['UPLOAD_FOLDER'], 'tp-01-02.jpeg')
	return render_template('home.html',user_image = full_filename,user_image1 = full_filename1,user_image2 = full_filename2,user_image3 = full_filename3,user_image4 = full_filename4,bg_image = full_filename5)


@app.route('/about')
def about():
    return '<h1>About Page</h1>' 


@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = Registration()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.pwd.data).decode('utf-8')
		user = User(fname = form.fname.data, lname = form.lname.data, usn = form.usn.data, pwd = hashed_password, email = form.email.data)
		db.session.add(user)
		db.session.commit()
		flash(f'Registered successfully', 'success')
		return redirect(url_for('login'))

	return render_template('register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = Login()
	if form.validate_on_submit():
		flash(f'Registered successfully', 'success')
		return redirect(url_for('home'))

	return render_template('login.html', form = form)#make html page called login.html


@app.route('/chat')
def chat():
	return render_template('chat.html')



########################################################################################################################
#####     SOCKET-IO ROUTES    #####
########################################################################################################################

@socketio.on('message')
def handle_msg(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

	
