from django.urls import path
from sql.views import *
app_name='something'

urlpatterns=[
    path('joins/',joins,name='joins'),
]