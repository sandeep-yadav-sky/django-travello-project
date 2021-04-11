from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # print request
    return render(request,'home.html',{'name':'kiran'}) 

def add(request):
    x=int(request.POST["num1"])
    y=int(request.POST["num2"])
    res=int(x+y)
    return render(request,"result.html",{'result':res})
    
    