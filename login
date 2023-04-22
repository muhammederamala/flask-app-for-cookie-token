<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/mystyle.css') }}">

</head>
<body>
    <nav class="navbar fixed-top">
        <h2>Flask app</h2>
    
    <div class="formbox">
  
    <form method="post" action="{{ url_for('login') }}">
        <h1 class="max"> Sign up </h1>
        <input type="text" class="max1" id="email" placeholder="username" name="username">
        <br>
        <input type="password" class="max1" id="password" placeholder="password" name="password">
        <br>
        <input type="submit" name="submit" class="max1" value="Login" id="submitid">
        <br>
    </form>
    </div>
</body>
</html>
