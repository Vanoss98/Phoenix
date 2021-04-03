from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from PIL import Image
import random

GENDER = (
    ('0','مرد'),
    ('1','زن'),
)

INTERESTS = (
    ('0','اطلاع رسانی'),
    ('1','درمان یا بازتوانی'),
    ('2','برگزاری ها'),
    ('3','حرفه ای و کاری'),
    ('4','مالی و اقتصادی'),
    ('5','غیره...'),
)

BURN_TYPE = (
    ('0','نوع سوختگی'),
    ('1','نوع اول'),
    ('2','نوع دوم'),
    ('3','نوع سوم'),
)

BURN_PERCENTAGE = (
    ('0','درجه سوختگی'),
    ('1','10%'),
    ('2','20%'),
    ('3','30%'),
)

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_regular = models.BooleanField(default=False)
    phoneNumber = models.IntegerField(null=True, blank=True, unique=True)
    city = models.CharField(max_length=100, blank=True)
    phoneHome = models.IntegerField(null=True, blank=True)
    address = models.TextField(max_length=500, blank=True)
    text = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=5, choices=GENDER, blank=True)
    interests = MultiSelectField(choices=INTERESTS, blank=True)
    birth = models.CharField(max_length=100, blank=True)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Regular(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    following = models.ManyToManyField(User, related_name='following', blank=True)
    burn_type = models.CharField(max_length=300, choices=BURN_TYPE, blank=True)
    burn_area = models.CharField(max_length=300, blank=True)
    burn_percentage = models.CharField(max_length=50, choices=BURN_PERCENTAGE, blank=True)
    burn_reason = models.CharField(max_length=300, blank=True)
    burn_place = models.CharField(max_length=300, blank=True)
    burn_date = models.CharField(max_length=50, blank=True)
    burn_question = models.CharField(max_length=300, blank=True)
    burn_text = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_following(self):
        return self.following.all()

    def get_following_users(self):
        following_list = [p for p in self.get_following()]
        return following_list

    def get_proposals_for_following(self):
        profiles = Profile.objects.all().exclude(user=self.user)
        followers_list = [p for p in self.get_following()]
        available = [p for p in profiles if p.user not in followers_list]
        random.shuffle(available)
        return available[:3]

    @property
    def following_count(self):
        return self.get_following().count()

    def get_followers(self):
        qs = Profile.objects.all()
        followers_list=[]
        for profile in qs:
            if self.user in profile.get_following():
                followers_list.append(profile)
        return followers_list

    @property
    def followers_count(self):
        return len(self.get_followers())

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)
