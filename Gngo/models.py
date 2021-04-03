from django.db import models
from django.db.models.base import Model
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


class Pishgiri(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    text = models.TextField(max_length=500)

class Darman(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    text = models.TextField(max_length=500)

class Baztavani(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    text = models.TextField(max_length=500)

class RavabetOmumi(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    text = models.TextField(max_length=500)

class Khayerin(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    text = models.TextField(max_length=500)

STATUS_CHOICES = (
    (0, 'active'),
    (1, 'deactive'),
) 

class Campaign(models.Model):
    objects = jmodels.jManager()
    name = models.CharField(max_length=200)
    slogan = models.CharField(max_length=200)
    summary = models.TextField(max_length=200)
    image = models.ImageField(upload_to='campaign_images', blank=True)
    image1 = models.ImageField(upload_to='campaign_images', blank=True)
    image2 = models.ImageField(upload_to='campaign_images', blank=True)
    image3 = models.ImageField(upload_to='campaign_images', blank=True)
    paragraph1 = models.TextField(blank=True)
    paragraph2 = models.TextField(blank=True)
    paragraph3 = models.TextField(blank=True)
    paragraph4 = models.TextField(blank=True)
    date = jmodels.jDateField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    tags = TaggableManager()
    slug = models.SlugField(unique=True, max_length=100)

class CampaignImages(models.Model):
    post = models.ForeignKey(Campaign, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='campaign_images', blank=True)