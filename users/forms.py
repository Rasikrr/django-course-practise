from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import CustomUser
from collections import OrderedDict



class LoginForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("email", "password")

    def validate_unique(self):
        pass


class CreateUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        )


class ProfileForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email"
        )

