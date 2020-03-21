from django.db import models
from datetime import date
from django import forms
from django.urls import reverse
from configration.models import AddSite, AddDepartment, AddCategory, AddDesignation, Rate
# Create your models here.


class EmployeeRegistration(models.Model):
    #Departmental Details
    
    EmpId = models.IntegerField(verbose_name='EmpId')
    Site = models.ForeignKey(AddSite,on_delete=models.CASCADE,max_length=150,verbose_name='Site')
    Department = models.ForeignKey(AddDepartment,on_delete=models.CASCADE,max_length=150,verbose_name='Department')
    Category = models.ForeignKey(AddCategory,on_delete=models.CASCADE,max_length=150,verbose_name='Category')
    Designation = models.ForeignKey(AddDesignation,on_delete=models.CASCADE,max_length=150,verbose_name='Designation')
    PfAllowance = models.BooleanField(default = True)
    EsiAllowance = models.BooleanField(default = True)
    Uan = models.PositiveIntegerField(null = False,verbose_name='Uan')
    Pf = models.PositiveIntegerField(null = True,verbose_name='Pf')
    AttendenceAward = models.BooleanField(default = True)
    AttendenceAllowance = models.BooleanField(default = True)
    ProfesionalTax = models.BooleanField(default = False)
    Rate = models.PositiveIntegerField(null = True)
    # Personal Details
    Name = models.CharField(max_length=150,verbose_name='Name')
    Father = models.CharField(max_length=150,verbose_name='Father')
    Dob = models.DateField()
    Gender = models.BooleanField(default = True)
    #Female = models.BooleanField(default = False)
    MaritalStatus = models.BooleanField(default = True)
    Address = models.CharField(max_length=200,verbose_name='Address')
    Aadhar = models.PositiveIntegerField(null=True)
    pan = models.CharField(max_length=10)
    choices = [('Working','WORKING'),('NotWorking','NOT WORKING')]
    Status = models.CharField(choices=choices,blank = False,max_length=10,verbose_name='Status')
    Doj = models.DateField(default = date.today)
    Doe = models.DateField(blank = True,verbose_name = 'Doe',null = True)

    def __str__(self):
        return '{name}'.format(name=self.Name)
    def get_absolute_url(self):
        return reverse("update",kwargs={"id":self.id})

class EmployeeRate(models.Model):
    EmpId = models.IntegerField(verbose_name='EmpId')
    Name = models.CharField(max_length=200,verbose_name='Name')
    Basic = models.IntegerField(verbose_name='Basic')
    Da = models.IntegerField(verbose_name='Da')
    Rate = models.IntegerField(verbose_name='Rate')
    Hra = models.IntegerField(verbose_name='Hra',null=True)
    Ca = models.IntegerField(verbose_name='Ca',null=True)
    SplAllow = models.IntegerField(verbose_name='SplAllow',null=True)
    CanteenAllow = models.IntegerField(verbose_name='CanteenAllow',null=True)

    def __str__(self):
        return '{name}_{EmpId}'.format(name=self.Name,EmpId=self.EmpId)
