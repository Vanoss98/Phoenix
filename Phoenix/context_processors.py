from Blog.forms import BaseContactForm
from django.conf import settings


def base_forms(request):
    return {       
        'info_form': BaseContactForm()
    }