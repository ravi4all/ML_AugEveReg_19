import cgi

form = cgi.FieldStorage()
review = form.getvalue("review")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

<h2>Review is {}</h2>

</body>
</html>
""".format(review))