<!DOCTYPE html>
<html lang="sv">
<head>
	<meta charset="UTF-8">
	<title>Wiki - Startsida</title>
</head>
<body>
	<h1><a href ="/">MaxWiki</a></h1>
	
	<p><a href ="/edit/">Vill du lägga till något?</a></p>
	
	%for art in wiki:
	<ul>
		<li>
		<a href ="/wiki/{{art[:-4]}}/">{{art [:-4]}}</a>
		</li>
	</ul>
	%end
	
	<h1>Ta bort:</h1>
	<form action="/delete/" method="POST">
		<input type="text" name="dele" id ="dele"/>
		<input type="submit" name="subit2" />
	</form>