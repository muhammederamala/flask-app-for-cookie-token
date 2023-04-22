# flask-app-for-cookie-token

File structure - 

project/
|-----app.py
|-----templates
|     |-----login.html
|     |-----secretscreen.html
|-----static/
|     |-----mystyle.css


Run the app.py file in a terminal. A login page will appear (login.html). Enter the credentials in the login page that comes up.

the login credentials are the following in the order (username,password) -
{ (john, password1),
  (max, password2),
  (mary, password3),
}

If successful, the page will be redirected to secretscreen.html and the unique tokens generated will be stored as cookies.
Next time, if you visit, you will be directly redirected to the secret screen rather than the login page.

