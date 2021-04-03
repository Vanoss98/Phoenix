from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django_jalali.db import models as jmodels

#----------------MAGHALAT-MODELS----------------#

class BaseContact(models.Model):
    info = models.TextField(max_length=100)


class HomeContact(models.Model):
    email = models.EmailField(blank=True)


class HomeGholak(models.Model):
    info = models.TextField(max_length=100)
    

class MaghaalaatPost(models.Model):
    objects = jmodels.jManager()
    title = models.CharField(max_length=250)
    paragraph1 = models.TextField(blank=True)
    paragraph2 = models.TextField(blank=True)
    paragraph3 = models.TextField(blank=True)
    paragraph4 = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images')
    paragraph5 = models.TextField(blank=True)
    paragraph6 = models.TextField(blank=True)
    paragraph7 = models.TextField(blank=True)
    paragraph8 = models.TextField(blank=True)
    important_part = models.TextField(blank=True)
    paragraph9 = models.TextField(blank=True)
    paragraph10 = models.TextField(blank=True)
    paragraph11 = models.TextField(blank=True)
    paragraph12 = models.TextField(blank=True)
    paragraph13 = models.TextField(blank=True)
    paragraph14 = models.TextField(blank=True)
    paragraph15 = models.TextField(blank=True)
    pdflink = models.TextField(blank=True)
    summ = models.TextField(max_length=200)
    pdf = models.FileField(upload_to='post_pdf')
   
    published = jmodels.jDateField()
    prof = models.CharField(max_length=100)
    tags = TaggableManager()
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = MaghaalaatPost.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)

class MaghaalaatImages(models.Model):
    post = models.ForeignKey(MaghaalaatPost, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='post_images', blank=True)

    def save(self, *args, **kwargs):
        try:
            this = MaghaalaatImages.objects.get(id=self.id)
            if this.images != self.images:
                this.images.delete(save=False)

        except:
            pass
        super().save(*args, **kwargs)

class MaghaalaatVideos(models.Model):
    post = models.ForeignKey(MaghaalaatPost, default=None, on_delete=models.CASCADE)
    videos = models.FileField(upload_to='post_videos', blank=True)

    def save(self, *args, **kwargs):
        try:
            this = MaghaalaatVideos.objects.get(id=self.id)

            if this.videos != self.videos:
                this.videos.delete(save=False)
                
        except:
            pass
        super().save(*args, **kwargs)

#----------------ANJOMAN-MODELS----------------#

class AnjomanPost(models.Model):
    objects = jmodels.jManager()
    title = models.CharField(max_length=250)
    paragraph1 = models.TextField(blank=True)
    paragraph2 = models.TextField(blank=True)
    paragraph3 = models.TextField(blank=True)
    paragraph4 = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images')
    paragraph5 = models.TextField(blank=True)
    paragraph6 = models.TextField(blank=True)
    paragraph7 = models.TextField(blank=True)
    paragraph8 = models.TextField(blank=True)
    important_part = models.TextField(blank=True)
    paragraph9 = models.TextField(blank=True)
    paragraph10 = models.TextField(blank=True)
    paragraph11 = models.TextField(blank=True)
    paragraph12 = models.TextField(blank=True)
    paragraph13 = models.TextField(blank=True)
    paragraph14 = models.TextField(blank=True)
    paragraph15 = models.TextField(blank=True)
    summ = models.TextField(max_length=200)
  
    published = jmodels.jDateField()
    prof = models.CharField(max_length=100)
    tags = TaggableManager()
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = AnjomanPost.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)

class AnjomanImages(models.Model):
    post = models.ForeignKey(AnjomanPost, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='post_images', blank=True)

    def save(self, *args, **kwargs):
        try:
            this = AnjomanImages.objects.get(id=self.id)
            if this.images != self.images:
                this.images.delete(save=False)

        except:
            pass
        super().save(*args, **kwargs)

class AnjomanVideos(models.Model):
    post = models.ForeignKey(AnjomanPost, default=None, on_delete=models.CASCADE)
    videos = models.FileField(upload_to='post_videos', blank=True)

    def save(self, *args, **kwargs):
        try:
            this = AnjomanVideos.objects.get(id=self.id)

            if this.videos != self.videos:
                this.videos.delete(save=False)
                
        except:
            pass
        super().save(*args, **kwargs)

#----------------SUKHTEGI-MODELS----------------#

class SukhtegiPost(models.Model):
    objects = jmodels.jManager()
    title = models.CharField(max_length=250)
    paragraph1 = models.TextField(blank=True)
    paragraph2 = models.TextField(blank=True)
    paragraph3 = models.TextField(blank=True)
    paragraph4 = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images')
    paragraph5 = models.TextField(blank=True)
    paragraph6 = models.TextField(blank=True)
    paragraph7 = models.TextField(blank=True)
    paragraph8 = models.TextField(blank=True)
    important_part = models.TextField(blank=True)
    paragraph9 = models.TextField(blank=True)
    paragraph10 = models.TextField(blank=True)
    paragraph11 = models.TextField(blank=True)
    paragraph12 = models.TextField(blank=True)
    paragraph13 = models.TextField(blank=True)
    paragraph14 = models.TextField(blank=True)
    paragraph15 = models.TextField(blank=True)
    summ = models.TextField(max_length=200)
    published = jmodels.jDateField()
    prof = models.CharField(max_length=100)
    tags = TaggableManager()
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = SukhtegiPost.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)

class SukhtegiImages(models.Model):
    post = models.ForeignKey(SukhtegiPost, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='post_images', blank=True)

    def save(self, *args, **kwargs):
        try:
            this = SukhtegiImages.objects.get(id=self.id)
            if this.images != self.images:
                this.images.delete(save=False)

        except:
            pass
        super().save(*args, **kwargs)

class SukhtegiVideos(models.Model):
    post = models.ForeignKey(SukhtegiPost, default=None, on_delete=models.CASCADE)
    videos = models.FileField(upload_to='post_videos', blank=True)

    def save(self, *args, **kwargs):
        try:
            this = SukhtegiVideos.objects.get(id=self.id)

            if this.videos != self.videos:
                this.videos.delete(save=False)
                
        except:
            pass
        super().save(*args, **kwargs)

#----------------STORIES-MODELS----------------#

class StoryPost(models.Model):
    objects = jmodels.jManager()
    title = models.CharField(max_length=250)
    paragraph1 = models.TextField(blank=True)
    paragraph2 = models.TextField(blank=True)
    paragraph3 = models.TextField(blank=True)
    paragraph4 = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images')
    paragraph5 = models.TextField(blank=True)
    paragraph6 = models.TextField(blank=True)
    paragraph7 = models.TextField(blank=True)
    paragraph8 = models.TextField(blank=True)
    important_part = models.TextField(blank=True)
    paragraph9 = models.TextField(blank=True)
    paragraph10 = models.TextField(blank=True)
    paragraph11 = models.TextField(blank=True)
    paragraph12 = models.TextField(blank=True)
    paragraph13 = models.TextField(blank=True)
    paragraph14 = models.TextField(blank=True)
    paragraph15 = models.TextField(blank=True)
    summ = models.TextField(max_length=200)
   
    published = jmodels.jDateField()
    prof = models.CharField(max_length=100)
    tags = TaggableManager()
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = StoryPost.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)


class StoryImages(models.Model):
    post = models.ForeignKey(StoryPost, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='post_images', blank=True)

    def save(self, *args, **kwargs):
        try:
            this = StoryImages.objects.get(id=self.id)
            if this.images != self.images:
                this.images.delete(save=False)

        except:
            pass
        super().save(*args, **kwargs)

class StoryVideos(models.Model):
    post = models.ForeignKey(StoryPost, default=None, on_delete=models.CASCADE)
    videos = models.FileField(upload_to='post_videos', blank=True)

    def save(self, *args, **kwargs):
        try:
            this = StoryVideos.objects.get(id=self.id)

            if this.videos != self.videos:
                this.videos.delete(save=False)
                
        except:
            pass
        super().save(*args, **kwargs)
