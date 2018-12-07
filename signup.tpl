<!DOCTYPE html>
<html>
<head>
	<title> Todo-ify </title>
	<link rel="stylesheet" href="/static/normalize.css">
	<link rel="stylesheet" type="text/css" href="/static/signupstylesheet.css">
</head>
<body>

<section>

<article>
	<h1>Todo-ify</h1>
	<form action="/signup" method="post">
		<input type="text" placeholder="Username" name="username" required>
    	<br>
   		<input type="text" placeholder="Display Name/Nickname" name="displayname" required>
   		<br>
   		<br>
		<input type="password" placeholder="Password" name="pass" required>
    	<br>
		<input type="password" placeholder="Confirm Password" name="confirmpass" required>

		<br>
		<br><br>
		<input type="submit" value="Sign Up"> <br><br>
	</form>
	<p>{{message}}</p>
</article>

<div id="signup">
	Already have an account? <a href="/login">Sign in</a>
</div>
	
<div id="pics">
<img src="/static/appstore.png">
<img src="/static/googleplay.png">
</div>
</section>
</body>
</html>