from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class TaxisForm(forms.ModelForm):
    class Meta:
        model = Taxis
        fields = ['user', 'phone', 'carNumber', 'carBrand', 'tariff', 'salary']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'carNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'carBrand': forms.TextInput(attrs={'class': 'form-control'}),
            'tariff': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['date', 'startTime', 'endTime', 'distance', 'cost', 'tariff' ,'passenger', 'taxis']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'startTime': forms.TextInput(attrs={'class': 'form-control'}),
            'endTime': forms.TextInput(attrs={'class': 'form-control'}),
            'distance': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.TextInput(attrs={'class': 'form-control'}),
            'tariff': forms.TextInput(attrs={'class': 'form-control'}),
            'passenger': forms.TextInput(attrs={'class': 'form-control'}),
            'taxis': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DateTimeForm(forms.ModelForm):
    class Meta:
        model = DateTime
        fields = ['date', 'time']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'})}

