from django import forms
from . import moels

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student_details
        fields = '__all__'
