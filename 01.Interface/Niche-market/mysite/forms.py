from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SingupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username","email","first_name","last_name", "password1", "password2",)

