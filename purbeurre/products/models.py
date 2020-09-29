from django.db import models
#toujours 1 espace avecnos imports et ceux de django
from .managers import ProductManager

# Create your models here.
class Category(models.Model):
    """table category for products"""
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Store(models.Model):
    """table store for products"""
    store_name = models.CharField(max_length=255)

    def __str__(self):
        return self.store_name


class Brand(models.Model):
    brand_name= models.CharField(max_length=255)

    def __str__(self):
        return self.brand_name



class Product(models.Model): # pour un produit uniquement
    """table product"""
    
    # prod_code = models.BigIntegerField(null=False, unique=True)
    prod_name = models.CharField(max_length=255)

    prod_category = models.ForeignKey(
                        Category,
                        on_delete = models.CASCADE
                        )
                        
    prod_store = models.ForeignKey(
                        Store,
                        on_delete = models.CASCADE
                        )
    prod_brand = models.ForeignKey(
                        Brand,
                        on_delete = models.CASCADE
                        )

    prod_nutrition_grade_fr = models.CharField(max_length=1)
    prod_image_nutrition_grade_fr = models.URLField(max_length=200)
    prod_image_nutrition_url = models.URLField(max_length=200, null=True)
    prod_url = models.URLField(max_length=200)
    prod_image_url = models.URLField(max_length=200)

    objects = ProductManager()


    def __str__(self):
        return f"{self.prod_name}, nutriscore: {self.prod_nutrition_grade_fr}"


class Favorite(models.Model):
    """table favorite
    as product substitute (new)
    and product substituted (product that has
    been replaced)"""
    substitute = models.ForeignKey(
                    Product,
                    on_delete = models.CASCADE,
                    verbose_name = "healthier",
                    related_name = "better_product",
                    )

    substituted = models.ForeignKey(
                    Product,
                    on_delete = models.CASCADE,
                    verbose_name = "been_replaced",
                    related_name = "avoid_it",
    )

    def __str__(self):
        return f"new:{self.substitute}, old:{self.substituted}"


