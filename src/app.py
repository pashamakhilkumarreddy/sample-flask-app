from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get('name', 'world')
    return render_template('home/index.html', name=name)

@app.route("/register")
def registerGet():
    return render_template('auth/register.html')

@app.route("/register", methods=['POST'])
def registerPost():
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return 'Fail'
    return render_template('success.html')