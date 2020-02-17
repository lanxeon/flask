from flask import Flask
app=Flask(__name__)

@app.route("/")
@app.route('/home')
def hello():
	return "<h1>waddup bitch" + str(534) + "lol nigga"+ "420 blaze it </h1>"
	
	
@app.route("/lol")
def lol():
	return "</h1>LOL</h1>"

if __name__=='__main__':
	app.run(debug=True)
