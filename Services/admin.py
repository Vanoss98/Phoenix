from Blog.models import HomeContact, HomeGholak
import django
from django.contrib import admin
from .models import DarmanService, BaztavaniService, GholakService, PishgiriService, MoshavereService, MadadKariService, KargahService, Namayande, Marakez, Pezashkan, Karyabi, Estekhdam


admin.site.register(DarmanService)
admin.site.register(BaztavaniService)
admin.site.register(PishgiriService)
admin.site.register(MoshavereService)
admin.site.register(MadadKariService)
admin.site.register(KargahService)
admin.site.register(GholakService)
admin.site.register(Karyabi)
admin.site.register(Estekhdam)

admin.site.register(Namayande)
admin.site.register(Marakez)
admin.site.register(Pezashkan)
admin.site.register(HomeContact)
admin.site.register(HomeGholak)
