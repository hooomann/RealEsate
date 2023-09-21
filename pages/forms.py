from django.forms import ModelForm
from django import forms
from .models import Contactu,Applicant
class ContactUsForm(ModelForm):
    class Meta:
        model=Contactu
        fields='__all__' 
        labels={
            'reasonforcontact':'Message',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.TextInput(attrs={'class':"form-control"}),
            'phone':forms.TextInput(attrs={'class':"form-control"}),
            'city':forms.TextInput(attrs={'class':"form-control"}),
            'reasonforcontact':forms.Textarea(attrs={'rows':3,'cols':30,'class':"form-control"})
        }
# Applicant form
class ApplicantForm(ModelForm):
    class Meta:
        model=Applicant
        fields='__all__'