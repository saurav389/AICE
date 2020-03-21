from django.shortcuts import render,redirect
from django.contrib import messages
from .models import AddCategory, AddDepartment, AddDesignation, AddSite, Rate
from .addsiteform import AddSiteForm 
# Create your views here.
def configure(request):
    obj1 = AddSite.objects.all()
    template_name = 'config.html'
    context = {"object":obj1}
    return render(request,template_name,context)

def AddSiteView(request,*args, **kwargs):
    if request.method == 'POST':
        site_form = AddSiteForm(request.POST)
        print("get")
        if site_form.is_valid():
     
            site_form.save()
            messages.success(request,'Successfully Updated')
            return redirect('profile')
        else:
            print('not valid form')
    else:
        print("post")
        site_form = AddSiteForm(instance=request.user)
    context = {
        'site_form':site_form
    }
    return render(request,"config.html",context)
def rateview(request,):
    obj1 = Rate.objects.get(pk=1)
    obj2 = Rate.objects.all()
    template_name = "config.html"
    context ={"object":obj2,
              "object2":obj1
              }
    return render(request,template_name,context)