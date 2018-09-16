from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
import requests
import json
from django.shortcuts import redirect
import datetime
from .models import *
# Create your views here.

def HomePage(request):
    return HttpResponse("<h1>ji</h1>")

def aboutPage(request):
    a=2
    b=4
    sum = a + b

    customers = getCustomers()
    for customer in customers:
        print(customer["_id"],getPurchases(str(customer["_id"])))
    return render(request,"HomePage/example.html",{"sum":sum})

def login(request):
    return render(request, "HomePage/login.html", {})

def categorySelection(request):
    return render(request,"HomePage/categorySelection.html",{})

def transactionUpdate(request):
    return render(request,"HomePage/transactionUpdate.html",{})

def signUp(request):
    print(reverse('signUp'))
    return render(request,"HomePage/signUp.html",{})

def dashboard(request):
    return render(request,"HomePage/dashboard.html",{})