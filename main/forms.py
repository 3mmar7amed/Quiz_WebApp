from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    ph = forms.CharField(label="phone number")
    grade = forms.IntegerField(label="grade")

    class Meta:
        model = User
        fields = ['first_name' , 'last_name','username', 'email', 'password1', 'password2' ,'grade','ph'  ]
