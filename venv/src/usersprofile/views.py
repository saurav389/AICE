from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .updateform import ProfileUpdationForm, UserUpdationForm

# Create your views here.
@login_required
def profile(request,*args, **kwargs):
    if request.method == 'POST':
        u_form = UserUpdationForm(request.POST,instance=request.user)
        p_form = ProfileUpdationForm(request.POST,request.FILES,instance=request.user.profile_view)
        print("get")
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Successfully Updated')
            return redirect('profile')
        else:
            print('not valid form')
    else:
        print("post")
        u_form = UserUpdationForm(instance=request.user)
        p_form = ProfileUpdationForm(instance=request.user.profile_view)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,"profile.html",context)
