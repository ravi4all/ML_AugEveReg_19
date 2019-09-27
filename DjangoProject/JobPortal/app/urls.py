from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("viewJobs",views.viewJobs,name='viewJobs'),
    path("devJobs",views.devJobs,name='devJobs'),
    path("registerUser",views.registerUser,name='registerUser')
]