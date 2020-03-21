from django import forms
from .models import EmployeeRegistration
from configration.models import AddSite,AddDepartment,AddDesignation,AddSite,AddCategory

class DateInput(forms.DateInput):
    input_type = 'date'

class regisForm(forms.ModelForm):
    
    class Meta:
        model = EmployeeRegistration
        fields = '__all__'
        widgets = {
        	'Dob':DateInput(),
            'Doj': DateInput(),
            'Doe': DateInput()
        }