from Users.models import User
import django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import BURN_PERCENTAGE, BURN_TYPE, User, Patient, Regular, GENDER, INTERESTS, Profile


class PatientCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.save()
        return User


class RegularCreationForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'* نام کاربری (انگلیسی)'
        }
        
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control6',
            'placeholder':'* کلمه رمز'
        }
        
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control6',
            'placeholder':'* تکرار کلمه رمز'
        }
        
    ))
    phoneNumber = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control6',
            'placeholder':'* تلفن همراه'
        }
        
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':' نام '
        }
        
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':' نام خانوادگی '
        }
        
    ))
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect(
        attrs={

        }
    ))

    interests = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=INTERESTS)

    phoneHome = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control6',
            'placeholder':' تلفن ثابت'
        }
        
    ))

    birth = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'تاریخ تولد'
        }
        
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control6',
            'placeholder':'ایمیل'
        }
    ))

    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'استان - شهر محل سکونت'
        }
        
    ))

    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'آدرس'
        }
        
    ))

    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'help-form-text',
            'placeholder': 'معرفی - شغل - توانمندی ها - تخصص ها - علاقه مندی ها',  
        }
    ))

    def clean_interests_field(self):
        return ','.join(self.cleaned_data['interests'])

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'phoneNumber', 'first_name', 'last_name', 'gender', 'phoneHome', 'birth', 'email', 'city', 'address', 'text', 'interests'] 


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_regular = True
        user.save()
        regular = Regular.objects.create(user=user)
        regular.save()
        return User


class UserUpadteForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'* نام کاربری (انگلیسی)'
        }
        
    ))
    
    phoneNumber = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control6',
            'placeholder':'* تلفن همراه'
        }
        
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':' نام '
        }
        
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':' نام خانوادگی '
        }
        
    ))
    
    phoneHome = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control6',
            'placeholder':' تلفن ثابت'
        }
        
    ))

    birth = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'تاریخ تولد'
        }
        
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control6',
            'placeholder':'ایمیل'
        }
    ))

    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'استان - شهر محل سکونت'
        }
        
    ))

    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'آدرس'
        }
        
    ))

    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'help-form-text',
            'placeholder': 'معرفی - شغل - توانمندی ها - تخصص ها - علاقه مندی ها',  
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'phoneNumber', 'first_name', 'last_name', 'phoneHome', 'birth', 'email', 'city', 'address', 'text'] 


class ProfileUpdateForm(forms.ModelForm):

    burn_type = forms.ChoiceField(choices=BURN_TYPE, required=False, widget=forms.Select(
        attrs={
            'class':'form-control6',
        }
    ))

    burn_area = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'ناحیه سوختگی'
        }
        
    ))

    burn_percentage = forms.ChoiceField(choices=BURN_PERCENTAGE, required=False, widget=forms.Select(
        attrs={
            'class':'form-control6',
        }
    ))

    burn_reason = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'دلیل سوختگی (نوع حادثه,...)'
        }  
    ))

    burn_place = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'محل وقوع سوختگی'
        }
        
    ))

    burn_date = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'تاریخ وقوع سوختگی'
        }
        
    ))

    burn_question = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control6',
            'placeholder':'تا به حال به چه مراکزی مراجعه کرده اید؟'
        }
    ))

    burn_text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'help-form-text',
            'placeholder': 'توضیحات بیشتر و تکمیلی',  
        }
    ))
    class Meta:
        model = Profile
        fields = ['image', 'burn_type', 'burn_area', 'burn_percentage', 'burn_reason', 'burn_place', 'burn_date', 'burn_question']

        