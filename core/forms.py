# forms.py
from django import forms
from core.models import User
# from core.forms import form 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
