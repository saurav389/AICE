from django.http import HttpResponse
from django.shortcuts import render
from .models import contactus
from .form import contactForm
# Create your views here.
def contact_view(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = contactForm
    context = {
        'form':form
    }
    return render(request,"contact.html",context)
    
