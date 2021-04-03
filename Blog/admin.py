from django.contrib import admin
from .models import AnjomanImages, AnjomanVideos, BaseContact, MaghaalaatImages, MaghaalaatPost, AnjomanPost, MaghaalaatVideos, StoryImages, StoryVideos, SukhtegiImages, SukhtegiPost, StoryPost, SukhtegiVideos
from django_jalali.admin.filters import JDateFieldListFilter


admin.site.register(BaseContact)


class BarAdmin(admin.ModelAdmin):
    list_filter = (
        ('published', JDateFieldListFilter),
    )
    prepopulated_fields = {'slug':('title',)}


#---------------MAGHAALAAT-ADMIN---------------#


class maghaalaatImagesAdmin(admin.StackedInline):
    model = MaghaalaatImages

class maghaalaatVideosAdmin(admin.StackedInline):
    model = MaghaalaatVideos
 
@admin.register(MaghaalaatPost)
class PostAdmin(admin.ModelAdmin):
    inlines = [maghaalaatImagesAdmin, maghaalaatVideosAdmin]
 
    class Meta:
       model = MaghaalaatPost


#---------------SUKHTEGI-ADMIN---------------#


class sukhtegiImagesAdmin(admin.StackedInline):
    model = SukhtegiImages

class sukhtegiVideosAdmin(admin.StackedInline):
    model = SukhtegiVideos
 
@admin.register(SukhtegiPost)
class PostAdmin(admin.ModelAdmin):
    inlines = [sukhtegiImagesAdmin, sukhtegiVideosAdmin]
 
    class Meta:
       model = SukhtegiPost


#---------------ANJOMAN-ADMIN---------------#


class anjomanImagesAdmin(admin.StackedInline):
    model = AnjomanImages

class anjomanVideosAdmin(admin.StackedInline):
    model = AnjomanVideos
 
@admin.register(AnjomanPost)
class PostAdmin(admin.ModelAdmin):
    inlines = [anjomanImagesAdmin, anjomanVideosAdmin]
 
    class Meta:
       model = AnjomanPost


#---------------STORY-ADMIN---------------#


class storyImagesAdmin(admin.StackedInline):
    model = StoryImages

class storyVideosAdmin(admin.StackedInline):
    model = StoryVideos
 
@admin.register(StoryPost)
class PostAdmin(admin.ModelAdmin):
    inlines = [storyImagesAdmin, storyVideosAdmin]
 
    class Meta:
       model = StoryPost