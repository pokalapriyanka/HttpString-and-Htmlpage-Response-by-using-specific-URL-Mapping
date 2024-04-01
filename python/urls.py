from django.urls import path
from python.views import *
app_name='anything'

urlpatterns=[
    path('function/',function,name='function'),
]