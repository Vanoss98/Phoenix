import django
from django.contrib import admin
from .models import Campaign, CampaignImages, Pishgiri, Darman, Baztavani, RavabetOmumi, Khayerin


admin.site.register(Pishgiri)
admin.site.register(Darman)
admin.site.register(Baztavani)
admin.site.register(RavabetOmumi)
admin.site.register(Khayerin)


class campaignImagesAdmin(admin.StackedInline):
    model = CampaignImages
 
@admin.register(Campaign)
class PostAdmin(admin.ModelAdmin):
    inlines = [campaignImagesAdmin]
 
    class Meta:
       model = Campaign