from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from .models import Product
from .forms import SearchedProduct

# Create your views here.
def index(request):
    latest_product_list = Product.objects.filter(id=1)
    context = {
        'latest_product_list' : latest_product_list,
    }
    return render(request, 'products/index.html', context)
    #products/index.html


def result(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'products/result.html', context)


def detail(request, product_id):
    product_details = Product.objects.filter(pk=product_id)
    context =  {
        'product_details': product_details,
    }
    return render(request, 'products/detail.html', context)


def favorites(request):
    return HttpResponse('These are your favorites of your session')


def process_search(request):

    try:
        if request.method == "POST":
            form = SearchedProduct(request.POST)

            if form.is_valid():
                search = form.cleaned_data["search"]
                search.save()
        else:
            form  =  SearchedProduct()

    except KeyError:
        print('pas de produit correspond, désolé')

        return render(request, 'products/detail.html', locals())
