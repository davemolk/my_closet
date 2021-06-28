from django.contrib import admin
from .models import Tag, OutfitTag, User, Clothing, Outfit

# Register your models here.

admin.site.register(Tag)
admin.site.register(OutfitTag)
admin.site.register(User)
admin.site.register(Clothing)
admin.site.register(Outfit)