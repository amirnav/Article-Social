from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
    username=forms.CharField(max_length=50,widget=forms.TextInput())
    email=forms.CharField(widget=forms.EmailInput())
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model=User
        fields=("username","email","password1")

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"input100"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"input100"}))

    def clean_password(self):
        user=authenticate(username=self.cleaned_data.get("username"),password=self.cleaned_data.get("password"))
        if user is not None:
            return self.cleaned_data.get("password")
        raise ValidationError("username and password are wrong",code="invalid_info")

class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("first_name","last_name","email","username")

