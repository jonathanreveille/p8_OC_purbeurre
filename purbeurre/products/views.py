from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render, redirect

from .models import Product
from .forms import SearchedProductForm

# Create your views here.
def home(request, search):
    form = SearchedProductForm()
    product_search = get_object_or_404(Product, Product.objects.filter(prod_name__icontains=search))
    context = {
        'product': product_search,
        'form': form,
    }
    return render(request, 'products/home.html', context)


def search(request):

    context = {}

    if request.method == "GET":
        form = SearchedProductForm(request.GET)

        if form.is_valid():
            product = form.cleaned_data.get("query_search")
            product_found = Product.objects.filter(prod_name__icontains=product) #et le nutritionscore pareil

            context = {
                'product':product,
                'product_found': product_found,
            }

        return  render(request, 'products/search.html', context)
        # product.object.find_subsitute ==> retrouver une liste de substitue possible

    else:
        form = SearchedProductForm()
        context = {
            'form' : form
        }

    return render(request, 'products/home.html', context)

# # new 22102020
def detail(request, product_id):

    """method to show product detail page"""

    product_details = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product_details
        }

    return render(request, 'products/detail.html', context)
