from django.contrib import admin
# Register your models here.
from .models import Product, Category, Brand, Favorite ,Store

admin.site.register(Category)
admin.site.register(Store)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Favorite)