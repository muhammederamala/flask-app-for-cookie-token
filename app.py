from flask import Flask, render_template, request, redirect, url_for, make_response
import secrets

app = Flask(__name__)

users = {
    "john": "password1",
    "max": "password2",
    "mary": "password3"
}

tokens = {}

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username in users and users[username] == password:
        resp = make_response(render_template('secretscreen.html'))
        resp.set_cookie('logged_in', 'true')
        return resp
    else:
        return render_template('login.html', error='Invalid username or password')

@app.route("/secretscreen")
def success():
    token = request.cookies.get("token") # get the token from the request
    if token in tokens:
        username = tokens[token] 
        return render_template("secretscreen.html", username=username)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    # Clear the 'name' cookie
    resp = make_response(render_template('login.html'))
    resp.set_cookie('name', '', expires=0)

    return resp

if __name__ == "__main__":
    app.run(debug=True)
