from django.contrib import admin
from .models import User, Patient, Regular, Profile


admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Regular)
admin.site.register(Profile)