from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def function(request):
    return HttpResponse('Functions is a independent block of code which is used for doing some specific task')
