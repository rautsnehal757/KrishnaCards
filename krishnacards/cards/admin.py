from django.contrib import admin

from .models import Categories,Cards,Carousel,CardsCategory
# Register your models here.

admin.site.register(Categories)
admin.site.register(Cards)
admin.site.register(Carousel)
admin.site.register(CardsCategory)
