from django.db import models


class ProductManager(models.Manager): # pour faire recherche pour tout les produits
    
    def creerlamethodequejeveux(self, parm1, parm2): #recherche de substitue
        pass

    def create_objects_from_openfoodfacts(self, category, product_list):
        """this method is to create product objects into our
        database"""
        from .models import Product, Category, Brand, Store

        categories = Category.objects.create(category_name=category)

        for product in product_list:
            brand = Brand.objects.create(brand_name=product["brands"])
            
            for store_name in product["stores"].split(","):
                store = Store.objects.create(store_name=store_name.strip().lower())

                Product.objects.create(
                                    prod_name=product["product_name"][:255],
                                    prod_nutrition_grade_fr=product["nutrition_grade_fr"],
                                    prod_image_nutrition_url=product["image_nutrition_url"],
                                    prod_url=product["url"],
                                    prod_image_url=product["image_front_url"],
                                    prod_brand=brand,
                                    prod_category=categories,
                                    prod_store=store,
                                )
