import flask
from flask import request, jsonify, Flask, render_template, redirect, url_for, redirect
import sqlite3
from flask_debugtoolbar import DebugToolbarExtension
import logging


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def home():
	return "Hello, World!!!"


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		completion = validate(email, password)

		if completion == False:
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', name='GET')



def validate(email, password):
	conn = sqlite3.connect('/home/mohit/Desktop/flask-project/registration/api_test.db')
	completion = False
	with conn:
		cur = conn.cursor()
		cur.execute("Select * from REGISTRATION")
		rows = cur.fetchall()
		for row in rows:
			db_email = row[1]  # email is in 2nd feature in the database table
			db_password = row[2] # password is 3rd feature in the database table
			if db_email == email:
				# completion = True
				completion = check_password(db_password, password)

	return completion



def check_password(hashed_password, password):
	return hashed_password == password



if __name__ == "__main__":
    app.run(debug=True)