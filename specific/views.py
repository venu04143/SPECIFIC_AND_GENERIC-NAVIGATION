from django.shortcuts import render

# Create your views here.

def sansa (request):
    return render(request,'sansa.html')

def arya(request):
    return render(request,'arya.html')