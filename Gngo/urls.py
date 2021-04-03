from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.aboutPage.as_view(), name='About-page'),
    path('maramname/', views.maramnamePage.as_view(), name='Maramname-page'),
    path('ketabche/', views.ketabchePage.as_view(), name='Ketabche-page'),
    path('komite-pishgiri/', views.pishgiri_form, name='Pishgiri-page'),
    path('komite-darman/', views.darman_form, name='Darman-page'),
    path('komite-baztavani/', views.baztavani_form, name='Baztavani-page'),
    path('komite-ravabet-omumi/', views.ravabet_form, name='Ravabet-page'),
    path('komite-khayerin/', views.khayerin_form, name='Khayerin-page'),

    path('campaigns/', views.cam_view, name='Campaign-page'),
    path("campaigns/posts/<int:id>/", views.cam_single, name="Campaign-detail"),
    path('campaigns/tag/<slug:slug>/', views.camtagged, name="camtagged"),
]
