from django.contrib import admin
from .models import Tag, OutfitTag, User, Top, Bottom, Dress, Shoe, Outerwear, Outfit

# Register your models here.


admin.site.register(Tag)
admin.site.register(OutfitTag)
admin.site.register(User)
admin.site.register(Top)
admin.site.register(Bottom)
admin.site.register(Dress)
admin.site.register(Shoe)
admin.site.register(Outerwear)
admin.site.register(Outfit)