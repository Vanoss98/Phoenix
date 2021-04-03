from django import forms
from .models import Contact, Help


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control2',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control2',
            'placeholder':'شهر / استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control2',
            'placeholder':'* تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control2',
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
        model = Contact
        fields = ('name','city','phone','email','text',)


HELP_CHOICES = (
    ('','چه نوع درخواستی دارید؟'),
    ('0','بنر‌های مراسم گرامیداشت'),
    ('1','اطلاع‌رسانی در فضای دیجیتال'),
    ('2','تخصصی (درمان - بازتوانی)'),
    ('3','کاری و اجرایی'),
)


class HelpForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'شهر / استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control6',
            'placeholder':'* شماره تماس'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control6',
            'placeholder':'ایمیل'
        }
    ))
    help = forms.ChoiceField(choices=HELP_CHOICES, required=False, widget=forms.Select(
        attrs={
            'class':'form-control6',
        }
    ))
    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'help-form-text',
            'placeholder': 'شرح درخواست',  
        }
    ))
    class Meta:
        model = Help
        fields = ('name','city','phone','email','text','help')