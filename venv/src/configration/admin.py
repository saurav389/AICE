from django.contrib import admin
from .models import AddSite, AddDepartment, AddDesignation, AddCategory, Rate
# Register your models here.
Mymodel = [AddSite,AddDepartment,AddDesignation,AddCategory,Rate]
admin.site.register(Mymodel)