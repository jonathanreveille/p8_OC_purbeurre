from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from .models import Product

# Create your views here.
def index(request):
    latest_product_list = Product.objects.filter(id=1)
    context = {
        'latest_product_list' : latest_product_list,
    }
    return render(request, 'products/index.html', context)

def result(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'products/result.html', context)

def details(request, product_id):
    return HttpResponse('You are looking at more details about the product %s.' %product_id)

def favorites(request):
    return HttpResponse('These are your favorites of your session')

# def vote(request):
    #return HttpResponse('Do you want to add this product to your favorites?')
#def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)