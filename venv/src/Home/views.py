from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request,"home.html",{})