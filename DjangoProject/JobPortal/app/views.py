from django.shortcuts import render
from django.http import HttpResponse
import pymysql

connection = pymysql.connect(host="localhost",port=3306,
user="root",database="bmpl_jobportal",autocommit=True)

cursor = connection.cursor()

# Create your views here.
# def index(request):
#     return HttpResponse("<h1>Hello World Using Django</h1>")

def index(req):
    return render(req, "index.html")

def viewJobs(req):
    query = "select * from jobs"
    cursor.execute(query)
    data = cursor.fetchall()
    return render(req, "viewJobs.html",{"data":data})

def devJobs(req):
    query = "select * from jobs where designation = 'Software Developer'"
    cursor.execute(query)
    data = cursor.fetchall()
    return render(req, "viewJobs.html",{"data":data})

def registerUser(req):
    username = req.POST['u_name']
    email = req.POST['u_email']
    pwd = req.POST['u_pwd']
    ph = req.POST['u_ph']

    query = "insert into users values (%s, %s, %s, %s)"
    cursor.execute(query, (email,username,pwd,ph))

    return render(req, 'home.html', {'name':username})