from django.urls import path
from . import views


urlpatterns = [
    path('contact-us/', views.contact_form, name='Contact-page'),
    path('help-us/', views.helpView.as_view(), name='Help-page'),
    path('help-us/help', views.help_form, name='Help-form-page'),
]
