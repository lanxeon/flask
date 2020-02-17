from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)

app.config['SECRET_KEY']='76dd3b2e5676f39be8d1c2adb6d382af'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sih.db'

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
lm=LoginManager(app)

lm.login_view='login'

from sih import routes