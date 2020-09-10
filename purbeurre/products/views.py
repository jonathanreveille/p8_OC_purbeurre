from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render, redirect
from .models import Product
from .forms import SearchedProduct

# Create your views here.
def home(request, search):
    form = SearchedProduct()
    product_search = get_object_or_404(Product, Product.objects.filter(prod_name__icontains=search))
    context = {
        'product': product_search,
        'form': form,
    }
    return render(request, 'products/home.html', context)

def search(request):

    context = {}

    if request.method == "GET":
        form = SearchedProduct(request.GET)

        if form.is_valid():
            product = form.save(commit=False)
            product = form.cleaned_data.get["search"] 
            product.save()
            product_found = Product.objects.filter(prod_name__icontains = product)
            context = {'product_found': product_found}

        return  render('products/search.html/', context)

    else:
        form = SearchedProduct()
        context = {
            'form' : form
        }

    return render(request, 'products/home.html', context)
