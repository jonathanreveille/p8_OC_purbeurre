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




# def results_from_search(request, product_id):

#     product_id = get_object_or_404(Product, pk=product_id)

#     if request.method == "GET":
#         product = request.POST.get("search")
#         form = SearchedProduct(product)
        
#         if form.is_valid() == True:
#             return HttpResponseRedirect("/products/1/detail")
#             # return HttpResponseRedirect("/products/result.html")
#     else:
#         form = SearchedProduct()

#     return render(request, 'products/1/detail/', {'form':form})


# def result(request, search):
#     user_search = request.POST.get(search)
#     searched = Product.objects.all.filter(prod_name__icontains=user_search)
#     product = get_object_or_404(Product, pk=searched.product_id)
#     context = {'product': product}
#     return render(request, 'products/1/detail/', context)




# def get_user_text(request):

#     product_search = request.GET["product_search"]
#     product = Product.objects.filter(prod_name__icontains=product_search)

#     return render(request, 'products/results' )



# def result_search(request):
#     """Django view search result page."""

#     try:
#         product_search = request.GET['product_search']
#         product = Product.objects.filter(
#             prod_name__icontains=product_search).first()
#         if product:
#             substitute = product.show_healthy_products()
#             return substitute

#         else:
#             product = None
#             substitute = None

#     except KeyError:
#         print('Pas de requête')

#     return render(
#         request,
#         'products/result.html',
#         {'product': product}
#     )



# def result_search(request):
#     """Django view search result page."""

#     result = None
#     try:
#         product_search = request.GET['q']
#         product = Product.objects.filter(
#             prod_name__icontains=product_search).first()
#         if product:
#             substituts = product.better_products()
#         else:
#             product = None
#             substituts = None                                                  
# # def get_results_from_search(request):
# #     if request.method == "GET":
# #         form = SearchedProduct(request.GET)
# #         if form.is_valid() == True:
# #             form_cleaned = form.cleaned_data(form)
# #             print('DEBUG1:', form_cleaned.your_name)
# #             print('DEBUG2:', form.your_name)
# #             return HttpResponseRedirect("/thanks/")
# #     else:
# #         form = SearchedProduct()

# #     return render(request, 'home.html', {'form': form})