from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'abhishek'})

def add(request):
    val1=request.POST["num1"]
    result=2+int(val1)
    return render(request, 'res.html', {'result':result})