<!DOCTYPE html>
<html>
<head>
	<title> Todo-ify </title>
	<link rel="stylesheet" href="/static/normalize.css">
	<link rel="stylesheet" type="text/css" href="/static/loginstylesheet.css">
</head>
<body>

<section>

<article>
	<h1>Todo-ify</h1>
	<form action="/login" method="post">
		<input type="text" placeholder="Username" name="username" required>
    	<br>
    	<br>
		<input type="password" placeholder="Password" name="pass" required>
		<br>
		<br><br>
		<input type="submit" value="Sign In"> <br><br>
	</form>
	<p>{{message}}</p>
</article>

<div id="signup">
	Don't have an account? <a href="/signup">Sign up</a>
</div>
	
<div id="pics">
<img src="/static/appstore.png">
<img src="/static/googleplay.png">
</div>
</section>
</body>
</html>