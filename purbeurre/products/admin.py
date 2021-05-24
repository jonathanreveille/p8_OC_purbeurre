from django.contrib import admin

from .models import Product, Brand, Category, Favorite


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Favorite)

