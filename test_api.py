import flask
from flask import request, jsonify, Flask, render_template
import sqlite3
# from flastext.mysql import MySQL

app = Flask(__name__)
app.config["DEBUG"] = True

# @app.route('/', methods=['GET'])
# def home():
#     return '''<h1>Distant Reading Archive</h1>
# <p>A prototype API for distant reading of science fiction novels.</p>'''


def insert_data(name, email, password, phone_number):
    # db_loc = '/home/mohit/Desktop/flask-project/api_test.db'
    conn = sqlite3.connect('/home/mohit/Desktop/flask-project/api_test.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO REGISTRATION(name, email, password, phone_number) VALUES (?, ?, ?, ?)", (name, email, password, phone_number))
    # con.execute("INSERT INTO REGISTRATION(name, email, password, phone_number) VALUES (abc, abc@gmail.com, abc@2310, 6464646)")
    conn.commit()

@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        # query_parameters = request.args
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form['phone_number']
        new_data = insert_data(str(name), str(email), str(password), str(phone_number))
        print("Success")
        return render_template('mine.html', name='GET')
    else:
        return render_template('mine.html', name='GET')
    # else:
        # return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)


# how to run:

# 1. python test_api.py (in sudo su)
# 2. in new terminal
# 2.1 open sqlite3 apt_test.db
# 2.2 select * from registration;