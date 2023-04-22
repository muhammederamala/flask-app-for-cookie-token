from flask import Flask, render_template, request, redirect, url_for, make_response
import secrets
import uuid
import jwt

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecretkey'
app.secret_key = 'mysecretkey'


users = {
    "john": "password1",
    "max": "password2",
    "mary": "password3"
}
logged_in_users = {}

tokens = {}

@app.route("/")
def index():
    token = request.cookies.get('logged_in_users') # get the token from the request
    if token in logged_in_users:
        username = logged_in_users[token] 
        return render_template("secretscreen.html", username=username)
    else:   
        return render_template("login.html")

@app.route("/login", methods=["GET","POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username in users and users[username] == password:
        token = str(uuid.uuid4())
        logged_in_users[token] = username
        # return redirect(url_for('success', token=token))


        # resp = make_response(redirect(url_for('success', token=token)))
        resp = make_response(render_template('secretscreen.html'))
        resp.set_cookie('logged_in_users', token)
        return resp
    

@app.route("/secretscreen",methods=["POST","GET"])
def success():
    token = request.cookies.get("token") # get the token from the request
    if token in logged_in_users:
        username = logged_in_users[token] 
        return render_template("secretscreen.html", username=username)
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    # Clear the 'name' cookie
    resp = make_response(render_template('login.html'))
    resp.set_cookie('name', '', expires=0)

    return resp

if __name__ == "__main__":
    app.run(debug=True)
