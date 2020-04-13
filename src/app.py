from flask import Flask, render_template, request, redirect, jsonify
import os
import smtplib
import csv

app = Flask(__name__)

# app.config.from_pyfile('settings.py')

students=[]

EMAIL = os.getenv("EMAIL")

PASSWORD = os.getenv('PASSWORD')

EMAIL_PORT = int(os.getenv('EMAIL_PORT'))

EMAIL_HOST = os.getenv('EMAIL_HOST')

WORDS = []

with open('large', 'r') as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())

@app.route("/")
def index():
    name = request.args.get('name', 'world')
    return render_template('home/index.html', name=name)

@app.route("/login")
def loginGet():
    return render_template('auth/login.html')

@app.route("/register")
def registerGet():
    return render_template('auth/register.html')

@app.route("/register", methods=['POST'])
def registerPost():
    name = request.form.get("name", None)
    email = request.form.get("email", None)
    password = request.form.get("password", None)
    if not name or not email or not password:
        return render_template('messages/errors/failure.html')
    student = dict()
    student['name'] = name
    student['email'] = email
    student['password'] = password
    students.append(student)
    file = open("users.csv", "a")
    writer = csv.writer(file)
    writer.writerow((name, email, password))
    file.close()
    message = "You are successfully registered"
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, email, message)
    return redirect('/users')

@app.route("/users")
def list_users():
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        students_csv = list(reader)
    return render_template('users/list_users.html', students=students_csv)

@app.route("/search")
def search():
    search_query = request.args.get("query", None)
    if search_query:
        words = [word for word in WORDS if word.startswith(search_query)]
        json_words = {
            'data': words
        }
        return jsonify(json_words)
    return render_template('search/index.html', words=[])

if __name__ == '__main_':
    app.run(debug=True, port=5000)