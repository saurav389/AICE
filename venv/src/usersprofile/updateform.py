from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile_view

class UserUpdationForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]
class ProfileUpdationForm(forms.ModelForm):
    class Meta:
        model = Profile_view
        fields = ['image']