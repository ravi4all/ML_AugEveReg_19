import sentimentAnalysis
import cgi
import csv

form = cgi.FieldStorage()

review = form.getvalue("review")
pred = sentimentAnalysis.test(review)

if pred == 0:
    msg = "Negative"
else:
    msg = "Positive"

with open('reviews.csv','a',newline='') as file:
    writer = csv.writer(file)
    writer.writerow([review,msg])

reviews = []
sentiments = []

with open('reviews.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        reviews.append(row[0])
        sentiments.append(row[1])

posCount = 0
negCount = 0

for i in range(len(sentiments)):
    if sentiments[i] == "Positive":
        posCount += 1
    else:
        negCount += 1

print("""
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['title', 'count'],
          ['Positive',     %s],
          ['Negative',      %s],
        ]);

        var options = {
          title: 'Movie Analysis'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>
</head>

<body>
<nav class="navbar navbar-dark bg-dark">
        <a class="navbar-brand" href="#">
            Review Analysis System (RAS)
        </a>
    </nav>

<div class="container">

"""%(posCount, negCount))

print("""
<h2>Prediction is {}</h2>
<p><b>Review is</b> : {}</p>
<hr>
""".format(msg,review))

print("""
<div class="row">
    <div class="col-md-6">
        <h2 class="text-center">Reviews So far</h2>
        <ul class="list-group">
""")

for i in range(len(reviews)):
    print("""
        <li class="list-group-item">{}</li>
    """.format(reviews[i]))

print("""
    </div>
    <div class="col-md-6">
        <h2 class="text-center">Reviews Analysis</h2>
        <h4>Positive Reviews : {}</h4>
        <h4>Negative Reviews : {}</h4>   
        <div id="piechart" style="width: 500px; height: 300px;"></div>     
    </div>
</div>
""".format(posCount, negCount))

print("""
</div>
</body>
</html>
""")