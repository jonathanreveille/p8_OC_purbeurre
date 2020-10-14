from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render, redirect
from django.urls import reverse

from .models import Product, Favorite
from .forms import SearchedProductForm

#Create your views here
def home(request, search):
    """View of home page of the application purbeurre"""

    form = SearchedProductForm()

    product_search = get_object_or_404(Product, Product.objects.filter(prod_name__icontains=search))
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
                prod_nutrition_grade_fr__lt="d",
                )[3:9]

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


def favorite(request):
    """method to create a favorite object
    from product_id and new substitute"""

    if request.method == "POST":
        user = request.user
        substitute_id = request.POST["favorite_id"]
        product_id = request.POST["id_product"]

        substitute = Product.objects.get(id=substitute_id)
        product_replaced = Product.objects.get(id=product_id)
        
        new_add_favorite = Favorite.objects.get_or_create(
            user=user,
            substitute=substitute,
            substituted=product_replaced,
        )

        context ={
            'product': substitute,
            'new_add_favorite':new_add_favorite,
        }

        return redirect('products:detail', product_id=substitute_id)
    
    return redirect('home') 



# def favorite(request):
#     """method to create a favorite object
#     from product_id and new substitute"""

#     if request.method == "GET":
#         form = AddProductToFavoriteForm(request.GET)

#         if form.is_valid():
#             favorite_id = form.cleaned_data.get("adding_a_product")
#             substitute = get_object_or_404(Product, Product.objects.filter(pk=favorite_id))

#             context = {
#                 'substitute': substitute,
#                 }

#         return render(request, 'products/favorite.html', context)


    #     user_id = request.user
    #     product_favorite = get_object_or_404(Product, id=product_id)
    #     product_name = product_favorite.prod_name
    #     product_replaced = product_id

    #     Favorite.objects.get(user=user_id, substitute=product_favorite, substituted=product_replaced)

    #     context = {
    #         'substitute': product_name,
    #     }

    # return redirect(request, "products/favorite.html", context)


# def like(request, product_id):
#     """method that helps the user to
#     add a product to his favorites"""

#     if request.method == "POST":
#         user_id = request.user
#         fav = get_object_or_404(Product, pk=product_id)

#         new_favorite_item = Favorite.objects.get_or_create(
#                             user=user_id,
#                             substitute=fav,
#                             replaced=product_id
#                             )

#         new_favorite_item.save()


    # try:
    #     product, substitute = (Product.objects.get(barcode=product_id),
    #                            Product.objects.get(barcode=substitute_id))
    # except (IntegrityError, Product.DoesNotExist):
    #     # if the product or substitute doesn't exist
    #     messages.info(request, "Produit ou substitut inexistant !")
    #     return redirect('/')

    # favorite = Favorite(user=user, product=product, substitute=substitute)