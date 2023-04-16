from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import client, LandOwner

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget = forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model= client
        fields = ('user','password1','password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise validationError("password does not match")
        

class clientRegistrationForm(UserCreationForm):
    pass
class LandOwnerRegistrationForm(UserCreationForm):
    pass