from django import db
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class ProductManager(db.models.Manager): # pour faire recherche pour tout les produits
    """class that will help the views to search in the db
    for products or to work with products objects"""
        
    def get_all_by_term(self, term):
        """method for autocomplete method to search in 
        db while user is typing his query search"""

        return self.filter(prod_name__icontains=term, 
                            prod_nutrition_grade_fr__lt="c",)[0:10]

    def find_products_from_db(self, product):
        """method to retrieve data from the database with
        the corresponding product that is searched"""

        product_found = models.Product.objects.filter( 
            prod_name__icontains=product,
            prod_nutrition_grade_fr__lt="c",
            )
        return product_found

    def create_paginator(self, product_found, per_page, request):
        """method for paginator generator for product in
        search.html. We will set with per_page param
        that only 6 products will be available on 1
        sheet"""

        paginator = Paginator(product_found, per_page)
        page_number = request.GET.get("page")
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.get_page(1)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)

        return page_obj

    def create_objects_from_openfoodfacts(self, category, product_list):
        """this method is to create product objects into
        our database"""

        category, created = models.Category.objects.get_or_create(category_name=category)

        for product in product_list:
            brand, created = models.Brand.objects.get_or_create(brand_name=product["brands"])
            
            product, created = models.Product.objects.get_or_create(
                                prod_url=product["url"],
                                defaults = {
                                    'prod_name' : product["product_name"][:255],
                                    'prod_nutrition_grade_fr' : product["nutrition_grade_fr"],
                                    'prod_image_nutrition_url' : product["image_nutrition_url"],
                                    'prod_image_url' : product["image_front_url"],
                                    'prod_brand' : brand,
                                    'prod_category' : category,
                                    })