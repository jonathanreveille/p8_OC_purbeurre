from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from .models import Product
from .forms import SearchedProduct

# Create your views here.

def home(request):
    form = SearchedProduct()
    context= {
        'form': form,
    }
    return render(request, 'products/home.html', context)

def index(request):
    # latest_product_list = Product.objects.filter(id=1)
    form =  SearchedProduct()
    context = {
        # 'latest_product_list' : latest_product_list,
        'form': form,
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


def search(request):

    form = SearchedProduct()

    try:
        product = request.POST["search"]
        data = Product.objects.filter(prod_name__icontains=product)

        if request.method == "POST":
            form = SearchedProduct(data)

            if form.is_valid():
                search = form.search
                search.save()
                # return HttpResponseRedirect(request, 'products/index.html')
                return HttpResponseRedirect(request, '/search/%s' %Product.id)
                
        else:
            form  =  SearchedProduct()
            return render(request, 'products/home.html', {"form":form})

    except KeyError:
        return render(request, 'products/home.html' %Product.id, {"form":form})


# def search(request):

#     form = SearchedProduct()

#     try:
#         user = Product.objects.filter(prod_name__icontains=request.POST["search"])
#         user.prod_name
        
#         if request.method == "POST":
#             form = SearchedProduct(selected_choice["search"])

#             if form.is_valid():
#                 search = form.search
#                 search.save()
#                 return HttpResponseRedirect(request, 'products/index.html')
#                 # return HttpResponseRedirect(request, 'products/%i' %Product.id)
                
#         else:
#             form  =  SearchedProduct()
#             return render(request, 'products/home.html', {"form":form})

#     except KeyError:
#         return render(request, 'products/home.html' %Product.id, {"form":form})


# def process_search(request):

#     form = SearchedProduct()
#     try:
#         selected_choice = Product.objects.filter(prod_name__icontains=request.POST["search"])
        
#         if request.method == "POST":
#             form = SearchedProduct(selected_choice["search"])

#             if form.is_valid():
#                 search = form.search
#                 search.save()
#                 return HttpResponseRedirect(request, 'products/%i' %Product.id, {"form":form})

#         else:
#             form  =  SearchedProduct()
#             return render(request, 'products/home.html', {"form":form})

#     except KeyError:
#         return render(request, 'products/%i' %Product.id)
