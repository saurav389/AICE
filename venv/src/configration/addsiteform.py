from django import forms
from .models import AddSite

class AddSiteForm(forms.ModelForm):
    class Meta:
        model = AddSite
        fields = ['site']