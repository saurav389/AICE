from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def login_view(request,*args, **kwargs):
    return render(request,"login.html",{})