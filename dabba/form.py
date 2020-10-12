from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import customer
from django.contrib.auth.forms import UserCreationForm

class registerForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    
    