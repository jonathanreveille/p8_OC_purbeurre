from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product
# Create your views here.

def complete(request):
    if request.method == "GET":
        searched_term = request.GET.get('term')
        products = Product.objects.get_all_by_term(searched_term)
        products = [product.prod_name for product in products]
        return JsonResponse(products, safe=False)