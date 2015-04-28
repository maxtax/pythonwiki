<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Wiki - Redigera</title>
	</head>
	<body>
	<h1><a href ="/">MaxWiki</a></h1>

		<h2>Redigera {{head}}:</h2>
		<form action="/update/" method="POST" accept-charset="UTF-8">
			<input type="text" name="subject" value = "{{head}}"/>
			<input type="text" name="data" value = "{{content}}"/>
			<input type="submit" name="submit" value="upload now" />
		</form>
	</body>
</html>