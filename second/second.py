from flask import Flask, render_template, url_for, redirect, request
from forms import SearchBar

app=Flask(__name__)
app.config['SECRET_KEY']='4f0c3cf5103e14d26b990afb4cae4f3e'


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

if __name__=='__main__':
	app.run(debug=True)