from django.db import models
from django.db.models.base import Model
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


class DarmanService(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    text = models.TextField(max_length=500)

class BaztavaniService(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    text = models.TextField(max_length=500)

class PishgiriService(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    text = models.TextField(max_length=500)

class MoshavereService(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    text = models.TextField(max_length=500)

class KargahService(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    text = models.TextField(max_length=500)

class MadadKariService(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    text = models.TextField(max_length=500)

class GholakService(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 

class Namayande(models.Model):
    markaz = models.CharField(max_length=50)
    ostan = models.CharField(max_length=50)
    shomare = models.CharField(max_length=30)
    masool = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    image = models.ImageField(upload_to='Namayande_images')

class Marakez(models.Model):
    markaz = models.CharField(max_length=50)
    ostan = models.CharField(max_length=50)
    shomare = models.CharField(max_length=30)
    masool = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    image = models.ImageField(upload_to='Marakez_images')

class Pezashkan(models.Model):
    markaz = models.CharField(max_length=50)
    ostan = models.CharField(max_length=50)
    shomare = models.CharField(max_length=30)
    takhasos = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    image = models.ImageField(upload_to='Pezeshkan_images')

genderfield = (
        ('male','مرد'),
        ('female','زن'),
    )

class Estekhdam(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField() 
    maharat = models.CharField(max_length=300)
    companyName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    saatKari = models.CharField(max_length=200)
    gender = models.CharField( max_length=10, choices=genderfield)


class Karyabi(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField( max_length=10, choices=genderfield)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField() 
    maharat = models.CharField(max_length=300)
    percentage = models.CharField(max_length=100)
    area = models.CharField(max_length=200)
    saatKari = models.CharField(max_length=200)