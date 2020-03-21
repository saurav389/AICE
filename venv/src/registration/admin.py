from django.contrib import admin
from .models import EmployeeRegistration,EmployeeRate
# Register your models here.
class register(admin.ModelAdmin):
	choices = [('WRK','WORKING'),('NTWRK','NOT WORKING')]
	fieldsets = (
        ('Departmental Info', {
            'fields': ('EmpId','Site','Department','Category','Designation','PfAllowance','EsiAllowance',
            			'Uan','Pf','AttendenceAward','AttendenceAllowance','ProfesionalTax','Rate')}),
        ('Personal Info', {
            'fields': ('Name','Father','Dob','Gender','MaritalStatus','Address','Aadhar','pan','Status','Doj')}),
    )
MyModels = [EmployeeRegistration]
admin.site.register(MyModels,register)
admin.site.register(EmployeeRate)