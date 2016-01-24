from flask import Flask, render_template, redirect, url_for, request, session, flash #g, commented out bc no more sqlight
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
# import sqlite3
from api_keys import SECRET_SESSION
from jellyDonut import *


app = Flask(__name__)

#need this for sessions to work right
app.secret_key = SECRET_SESSION

#this was for using straight up sqlight
#app.database = "sample.db"

#change to sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

#create the sqlalchemy object
db = SQLAlchemy(app)

#only now can we import the model, bc only now the db object exists
from models import * #by * we mean BlogPost, but whatever

#route for home
@app.route('/')
def home():
    return render_template ("welcome.html")
    #now, using squalchemy- fancy cause it's one line:
    posts = db.session.query(BlogPost).all()
    return render_template ("index.html", posts = posts)

#route for welcome
@app.route('/wtf')
def welcome():
	return render_template ("wtf.html")

#start the server with 'run()' method
if __name__ == '__main__':
	app.run(debug=True)