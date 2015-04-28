<!DOCTYPE html>
<html lang="sv">
<head>
	<meta charset="UTF-8">
	<title>Wiki - Lägg till</title>
</head>
<body>
    <h1><a href ="/">MaxWiki</a></h1>
	<h2>Lägg till:</h2>
        <form action="/update/" method="POST" accept-charset="UTF-8">
            <input type="text" name="subject" />
            <input type="text" name="data"/>
            <input type="submit" name="submit" value="upload now" />
        </form>
</body>
</html>