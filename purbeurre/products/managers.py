from django import db
from . import models


class ProductManager(db.models.Manager): # pour faire recherche pour tout les produits

    # def create_objects_from_openfoodfacts(self, category, product_list):
    #     """this method is to create product objects into our
    #     database"""

    #     categories = models.Category.objects.create(category_name=category)

    #     for product in product_list:
    #         brand = models.Brand.objects.create(brand_name=product["brands"])

    #         product = models.Product.objects.get_or_create(
    #                             prod_name=product["product_name"][:255],
    #                             prod_nutrition_grade_fr=product["nutrition_grade_fr"],
    #                             prod_image_nutrition_url=product["image_nutrition_url"],
    #                             prod_url=product["url"],
    #                             prod_image_url=product["image_front_url"],
    #                             prod_brand=brand,
    #                             prod_category=categories,
    #                             # prod_store=store,
    #                         )
                        
    #         for store_name in product["stores"].split(","):
    #             models.Store.objects.get_or_create(store_name=store_name.strip().lower())

  
    def create_objects_from_openfoodfacts(self, category, product_list):
        """this method is to create product objects into our
        database"""

        categories = models.Category.objects.create(category_name=category)

        for product in product_list:
            brand = models.Brand.objects.create(brand_name=product["brands"])
            
            for store_name in product["stores"].split(","):
                store = models.Store.objects.create(store_name=store_name.strip().lower())

                models.Product.objects.get_or_create(
                                    prod_name=product["product_name"][:255],
                                    prod_nutrition_grade_fr=product["nutrition_grade_fr"],
                                    prod_image_nutrition_url=product["image_nutrition_url"],
                                    prod_url=product["url"],
                                    prod_image_url=product["image_front_url"],
                                    prod_brand=brand,
                                    prod_category=categories,
                                    prod_store=store,
                                )


    # def creerlamethodequejeveux(self, parm1, parm2): #recherche de substitue
    #     passs