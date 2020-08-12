from django import forms
from .models.customer import Customer 
from django.forms import ModelForm


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname',  'email', 'password']