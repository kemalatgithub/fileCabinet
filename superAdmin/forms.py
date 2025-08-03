from django import forms
from django.forms import ModelForm, TextInput, EmailInput, FileInput
from django.contrib.auth.models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'permissions']
           