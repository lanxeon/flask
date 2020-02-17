from flask import Flask,render_template,url_for
import os

IMAGE_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER


@app.route('/')
@app.route('/home')
def hello_world():
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

if __name__=='__main__':
	app.run(debug=True)