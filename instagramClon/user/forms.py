from django import forms
from user.models import User
from django.forms import ModelForm

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','username','password']
        widgets = {
            'password': forms.PasswordInput
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
