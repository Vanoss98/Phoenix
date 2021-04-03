from django import forms
from .models import DarmanService, BaztavaniService, GholakService, Karyabi, PishgiriService, KargahService, MadadKariService, MoshavereService, Estekhdam, genderfield


class DarmanServiceForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'شهر/استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control1',
            'placeholder':'ایمیل'
        }
    ))
    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'darman-service-form-text',
            'placeholder': '* متن درخواست',  
        }
    ))

    class Meta:
        model = DarmanService
        fields = ('name','city','phone','email','text',)

class BaztavaniServiceForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'شهر/استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control1',
            'placeholder':'ایمیل'
        }
    ))
    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'darman-service-form-text',
            'placeholder': '* پیام, سوال, نظر, درخواست...',  
        }
    ))

    class Meta:
        model = BaztavaniService
        fields = ('name','city','phone','email','text',)

class PishgiriServiceForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'شهر/استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control1',
            'placeholder':'ایمیل'
        }
    ))
    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'darman-service-form-text',
            'placeholder': '* پیام, سوال, نظر, درخواست...',  
        }
    ))

    class Meta:
        model = PishgiriService
        fields = ('name','city','phone','email','text',)

class KargahServiceForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'شهر/استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control1',
            'placeholder':'ایمیل'
        }
    ))
    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'darman-service-form-text',
            'placeholder': '* پیام, سوال, نظر, درخواست...',  
        }
    ))

    class Meta:
        model = KargahService
        fields = ('name','city','phone','email','text',)

class MadadKariServiceForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'شهر/استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control1',
            'placeholder':'ایمیل'
        }
    ))
    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'darman-service-form-text',
            'placeholder': '* پیام, سوال, نظر, درخواست...',  
        }
    ))

    class Meta:
        model = MadadKariService
        fields = ('name','city','phone','email','text',)

class MoshavereServiceForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'شهر/استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control1',
            'placeholder':'ایمیل'
        }
    ))
    text = forms.Field(widget=forms.TextInput(
        attrs={
            'class':'darman-service-form-text',
            'placeholder': '* پیام, سوال, نظر, درخواست...',  
        }
    ))

    class Meta:
        model = MoshavereService
        fields = ('name','city','phone','email','text',)

class GholakServiceForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* نام و نام خانوادگی'
        }
        
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'شهر/استان',
        }
      
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control1',
            'placeholder':'ایمیل'
        }
    ))

    class Meta:
        model = GholakService
        fields = ('name','city','phone','email',)


class EstekhdamForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control3',
            'placeholder':'* نام و نام خانوادگی استخدام کننده'
        }
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control3',
            'placeholder':'* شهر/استان'
        }
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control3',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control3',
            'placeholder':'ایمیل'
        }
    ))
    
    maharat = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control3',
            'placeholder':'* مهارت یا کار مورد نظر'
        }
    ))

    companyName = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control3',
            'placeholder':'* نام شرکت'
        }
    ))

    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control3',
            'placeholder':'* آدرس محل کار'
        }
    ))

    saatKari = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control3',
            'placeholder':'* زمان کاری مطلوب'
        }
    ))

    gender = forms.ChoiceField(choices=genderfield, widget=forms.RadioSelect(
        attrs={

        }
    ))

    class Meta:
        model = Estekhdam
        fields = ('name','city','phone','email','maharat','companyName','address','saatKari','gender',)

class KaryabiForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* نام و نام خانوادگی'
        }
    ))

    gender = forms.ChoiceField(choices=genderfield, widget=forms.RadioSelect(
        attrs={

        }
    ))

    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* شهر/استان'
        }
    ))
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* شماره تلفن'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control1',
            'placeholder':'ایمیل'
        }
    ))
    
    maharat = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'* مهارت یا کار مورد نظر'
        }
    ))

    percentage = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'درصد سوختگی'
        }
    ))

    area = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'ناحیه سوختگی'
        }
    ))

    saatKari = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control1',
            'placeholder':'زمان کاری مطلوب'
        }
    ))

    

    class Meta:
        model = Karyabi
        fields = ('name','city','phone','email','maharat','percentage','area','saatKari','gender',)


   