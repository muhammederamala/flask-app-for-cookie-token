# flask-app-for-cookie-token

File structure - 

project/
|-----app.py
|-----templates
|     |-----login.html
|     |-----secretscreen.html
|-----static/
|     |-----mystyle.css


Run the app.py file in a terminal. Enter the credentials in the login page that comesup.

the login credentials are the followig -
{ (john, password1),
  (max, password2),
  (mary, password3),
}

If successful, the page will be redirected to ssecretscreen.html and the unique tokens generated will be stored as cookies.
Next time, if you visit, you will be directly redirected to the secret screen.

