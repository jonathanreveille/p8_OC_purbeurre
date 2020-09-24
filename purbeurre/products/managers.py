from django.db import models

class ProductManager(models.Manager): # pour faire recherche pour tout les produits
    
    def creerlamethodequejeveux(self, parm1, parm2): #recherche de substitue
        pass

    def show_healthy_products(self):
        """Retrieve healthier products from bdd
        from user's query search"""
        from .models import Product
        
        p = Product()
        return p.objects.filter(prod_category=self.prod_category, prod_nutrition_grade_fr__lt=self.prod_nutrition_grade_fr)