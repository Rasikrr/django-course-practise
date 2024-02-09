from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from users.models import CustomUser
from collections import OrderedDict



class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("email", "password")

    def validate_unique(self):
        pass