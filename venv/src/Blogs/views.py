from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blogs_view(request,*args, **kwargs):
    return render(request,"blogs.html",{})