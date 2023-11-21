from django.shortcuts import render

# Create your views here.

def jonsnow(request):
    return render(request,'jonsnow.html')

def  robb(request):
    return render(request,'robb.html')