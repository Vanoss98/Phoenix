import django
from django.contrib import admin
from .models import Contact, Help


admin.site.register(Contact)
admin.site.register(Help)