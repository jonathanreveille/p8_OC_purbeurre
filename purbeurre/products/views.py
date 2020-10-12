from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render, redirect

from .models import Product, Favorite
from .forms import SearchedProductForm

# Create your views here.
def home(request, search):
    """View of home page of the application purbeurre"""

    form = SearchedProductForm()

    product_search = get_object_or_404(Product, Product.objects.filter(category_name_prod_name__icontains=search))
    context = {
        'product': product_search,
        'form': form,
    }

    return render(request, 'products/home.html', context)


def search(request):
    """view that corresponds to the search bar zone,
    that allows to retrieve data from the DB
    according the user's query"""

    context = {}

    if request.method == "GET":
        form = SearchedProductForm(request.GET)

        if form.is_valid():
            product = form.cleaned_data.get("query_search")
            product_found = Product.objects.filter(
                prod_name__icontains=product,
                prod_nutrition_grade_fr__lt="c"
                )[:15]

            context = { 
                'product':product,
                'product_found': product_found,
            }

        return  render(request, 'products/search.html', context)

    else:
        form = SearchedProductForm()
        context = {
            'form' : form
        }

    return render(request, 'products/home.html', context)

# # new 22102020
def detail(request, product_id):
    """view about detail page of a product"""

    product_details = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product_details
        }

    return render(request, 'products/detail.html', context)


