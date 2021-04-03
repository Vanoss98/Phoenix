from django.urls import path
from . import views


urlpatterns = [
  path('darman/', views.darman_service_form, name='Darman-serv-page'),
  path('baztavani/', views.baztavani_service_form, name='Baztavani-serv-page'),
  path('pishgiri/', views.pishgiri_service_form, name='Pishgiri-serv-page'),
  path('kargah-amuzeshi/', views.kargah_service_form, name='Kargah-serv-page'),
  path('madad-kari/', views.madadkari_service_form, name='Madadkari-serv-page'),
  path('moshavere/', views.moshavere_service_form, name='Moshavere-serv-page'),
  path('gholak/', views.gholak_service_form, name='Gholak-page'),
  path('namayndegan/', views.nmp_view, name='npm-page'),
  path('karyabi/', views.MyView.as_view(), name='Karyabi-page'),
] 
