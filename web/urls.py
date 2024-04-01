from django.urls import path
from web.views import *
app_name='anything'

urlpatterns=[
    path('tag/',tag,name='tag'),
]