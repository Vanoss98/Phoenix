from django import forms
from .models import BaseContact, HomeContact, HomeGholak


class BaseContactForm(forms.ModelForm):
    info = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control7',
            'placeholder':'ایمیل یا شماره تلفن خود را وارد کنید'
        } 
    ))
  
    class Meta:
        model = BaseContact
        fields = ('info',)


class HomeContactForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control8',
            'placeholder':'ایمیل خود را وارد کنید'
        } 
    ))
  
    class Meta:
        model = HomeContact
        fields = ('email',)


class HomeGholakForm(forms.ModelForm):
    info = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control9',
            'placeholder':'ایمیل یا شماره تلفن'
        } 
    ))
  
    class Meta:
        model = HomeGholak
        fields = ('info',)        