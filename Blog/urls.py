from django.urls import path, re_path
from . import views
from .views import MainListView, Medics, Questions, Statistics, info

urlpatterns = [
    path('', MainListView.as_view(), name='Home-Page'),
    path('statistics/', Statistics.as_view(), name='Stats-page'),
    path('medic/', Medics.as_view(), name='Medic-page'),
    path('common-questions/', Questions.as_view(), name='Questions-page'),
    path('info/', info, name='base'),

    path('maghaalaat/', views.MaghaleMain.as_view(), name="blog-page"),
    path('maghaalaat/tags/<slug:tag_slug>/', views.MaghaleTags.as_view(), name="tagged"),
    re_path(r'maghaalaat/(?P<the_slug>[-\w]+)/', views.MaghaleDetail.as_view(), name='post-detail'),

    path('havaades/', views.SukhtegiMain.as_view(), name="news-sukhtegi-page"),
    path('havaades/tags/<slug:tag_slug>/', views.SukhtegiTags.as_view(), name="etagged"),
    re_path(r'havaades/(?P<the_slug>[-\w]+)/', views.SukhtegiDetail.as_view(), name='news-sukhtegi-detail'),

    path('anjoman/', views.AnjomanMain.as_view(), name="news-anjoman-page"),
    path('anjoman/tags/<slug:tag_slug>/', views.AnjomanTags.as_view(), name="gtagged"),
    re_path(r'anjoman/(?P<the_slug>[-\w]+)/', views.AnjomanDetail.as_view(), name='news-anjoman-detail'),

    path('stories/', views.StoryMain.as_view(), name="stories-page"),
    path('stories/tags/<slug:tag_slug>/', views.StoryTags.as_view(), name="stagged"),
    re_path(r'stories/(?P<the_slug>[-\w]+)/', views.StoryDetail.as_view(), name='stories-detail'),

]