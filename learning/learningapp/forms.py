from learningapp.models import UserDetails
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ['username','email','password',]

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['phone','address','street','city','zipcode','userpic']