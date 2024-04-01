from django.shortcuts import render

# Create your views here.
def tag(request):
    return render(request,'tag.html')