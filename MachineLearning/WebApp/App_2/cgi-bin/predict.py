import cgi
import linearRegression

form = cgi.FieldStorage()

gender = int(form.getvalue('gender'))
per10 = float(form.getvalue('10per'))
per12 = float(form.getvalue('12per'))
tier = int(form.getvalue('tier'))
degree = int(form.getvalue('degree'))
gpa = int(form.getvalue('gpa'))
english = int(form.getvalue('eng'))
logical = int(form.getvalue('logical'))
quant = int(form.getvalue('quant'))

pred = linearRegression.test(gender,per10,per12,tier,degree,gpa,english,logical,quant)

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

<h2>Prediction is {}</h2>

</body>
</html>
""".format(pred))
