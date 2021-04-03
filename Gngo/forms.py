from django import forms
from .models import Baztavani, Pishgiri, Darman, RavabetOmumi, Khayerin


class PishgiriForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'شهر/استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'ایمیل'
        }
    ))
    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'pishgiri-form-text',
            'placeholder': '* پیام, سوال, نظر, درخواست...',  
        }
    ))

    class Meta:
        model = Pishgiri
        fields = ('name','city','phone','email','text',)

class DarmanForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'شهر/استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'ایمیل'
        }
    ))
    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'pishgiri-form-text',
            'placeholder': '* پیام, سوال, نظر, درخواست...',  
        }
    ))

    class Meta:
        model = Darman
        fields = ('name','city','phone','email','text',)

class BaztavaniForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'شهر/استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'ایمیل'
        }
    ))
    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'pishgiri-form-text',
            'placeholder': '* پیام, سوال, نظر, درخواست...',  
        }
    ))

    class Meta:
        model = Baztavani
        fields = ('name','city','phone','email','text',)

class RavabetOmumiForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'شهر/استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'ایمیل'
        }
    ))
    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'pishgiri-form-text',
            'placeholder': '* پیام, سوال, نظر, درخواست...',  
        }
    ))

    class Meta:
        model = RavabetOmumi
        fields = ('name','city','phone','email','text',)

class KhayerinForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'شهر/استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'ایمیل'
        }
    ))
    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'pishgiri-form-text',
            'placeholder': '* پیام, سوال, نظر, درخواست...',  
        }
    ))

    class Meta:
        model = Khayerin
        fields = ('name','city','phone','email','text',)








        