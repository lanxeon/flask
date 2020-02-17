from flask import render_template, url_for, redirect, request
from third.forms import SearchBar
from third import app

data= [
{
	'name': "osama",
	'eye' : "wide",
	'nose': "crooked",
	'lip' : 'slim',
},
{
	'name': "al baghdadi",
	'eye' : "narrow",
	'nose': "straight",
	'lip' : 'wide',
}
]


@app.route("/", methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def hello():
	find=SearchBar()
	if find.validate_on_submit():
	#if request.method == 'POST':
		return redirect(url_for('found'))
	return render_template('home.html', data=data, find=find)
	
	

@app.route('/found')
def found():
	return "<h1>Data Found</h1>"

	
	
@app.route("/lol", methods=['GET','POST'])
def lol():
	find=SearchBar()
	if find.validate_on_submit():
		return redirect(url_for('found'))
	return render_template("lol.html", title='lol', find=find)