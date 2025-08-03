from django import forms
from django.forms import ModelForm, PasswordInput, Select, TextInput, EmailInput, FileInput
from app.models import CustomUser

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','password','user_profile']
        widgets = {
            'first_name_label': 'የመጀመሪያ ስም',
            'first_name': TextInput(attrs={
                'class': "form-control form-control-border col-md-6",
                'style': 'max-width: 2000px; width:500px',
                'placeholder': 'የመጀመሪያ ስም',
                }),

            'last_name': TextInput(attrs={
                'class': "form-control form-control-border col-md-6",
                'style': 'max-width: 1200px;width:500px;',
                'placeholder': 'የአባት ስም'
                }),
            'email': EmailInput(attrs={
                'class': "form-control form-control-border col-md-6 ", 
                'style': 'max-width: 1200px;width:500px;',
                'placeholder': 'እሜይል'
                }),

            'password': PasswordInput(attrs={
                'class': "form-control form-control-border col-md-6",
                'style': 'max-width: 1200px;width:500px;',
                'placeholder': 'የይለፍ ቃል'
                }),
            'user_profile': FileInput(attrs={
                'class': "form-control form-control-border col-md-6",
                'style': 'max-width: 2000px; width:500px',
                'placeholder': 'ፕሮፋይል ፎቶ',
                }),

        }