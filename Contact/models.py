from django.db import models
from django.db.models.base import Model
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


class Contact(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    text = models.TextField(max_length=500)


HELP_CHOICES = (
    ('0','بنر‌های مراسم گرامیداشت'),
    ('1','اطلاع‌رسانی در فضای دیجیتال'),
    ('2','تخصصی (درمان - بازتوانی)'),
    ('3','کاری و اجرایی'),
)


class Help(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) 
    help = models.CharField(max_length=300, choices=HELP_CHOICES)
    text = models.TextField(max_length=500)