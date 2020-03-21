from django.shortcuts import render, redirect
from .regform import regisForm
from django.http import HttpResponse
from configration.models import AddSite, AddCategory,Rate
from .models import EmployeeRegistration, EmployeeRate
import random
# Create your views here.   
def ids():
    no = EmployeeRegistration.objects.count()
    employee = EmployeeRegistration.objects.all()
    empid = random.randint(no,100000)
    next = no + empid
    for data in employee:
        if(data.id == empid):
            pass
        else:
            empid = random.randint(no,next)
    if(empid == None):
        number = 1
        return number
    else:
        number = empid
        return number
def EmployeeList(request):
    st=request.user.profile_view.site
    context = {'employeelist':EmployeeRegistration.objects.filter(Site=st)}
    return render(request,"employeelist.html",context)
def EmployeeDelete(request,id):
    employee = EmployeeRegistration.objects.get(pk=id)
    employee.delete()
    return redirect('/register/list')

def registration_view(request,id=0):
    emp_id = ids()
    EmployeeId={"EmpId":emp_id}
    if(request.method == 'POST'):
        if(id==0):
            form = regisForm(request.POST or None,initial=EmployeeId)
        else:
            employee = EmployeeRegistration.objects.get(pk=id)
            form = regisForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            form = regisForm(initial=EmployeeId)
            return redirect('/register/list') 
    else:
        if(id==0):
            form = regisForm(initial=EmployeeId) 
        else:
            employee = EmployeeRegistration.objects.get(pk=id)
            form = regisForm(instance=employee)
        context = {
            'form':form,
            "contact":"active"
        }
        return render(request,"registration.html",context)

def EmployeeRateView(request,*args,**kwargs):
    rate = Rate.objects.all()
    emp = EmployeeRegistration.objects.all()
    data = {}
    if request.method == 'POST':
        for employee in emp:
            for item in rate:
                if(employee.Site==item.site and employee.Category == item.category):
                    basic=item.rate
                    da=0
                    total = basic+da
                    check = EmployeeRate.objects.filter(EmpId=employee.EmpId).exists()
                    print(check)
                    if(check is False):
                        save_employeerate = EmployeeRate.objects.create(EmpId=employee.EmpId,Name=employee.Name,Basic=item.rate,Da=da,Rate=total)
                        #data = {
                        #"EmpId":employee.EmpId,
                        #"Name":employee.Name,
                        #"Basic":item.rate,
                        #}
    context = {'employeedetail':EmployeeRate.objects.all()}

    return render(request,"employeerate.html",context)

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