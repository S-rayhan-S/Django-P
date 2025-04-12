from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from App_Login.models import User, Profile  # Importing my custom models


# forms

class Profileform(ModelForm):
    class Meta:
        model=Profile
        exclude=('user',)
        
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=('email','password1','password2',)














