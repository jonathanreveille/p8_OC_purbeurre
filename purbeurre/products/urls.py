from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "products"

urlpatterns = [
    # ex: /products/
    path('', TemplateView.as_view(template_name='products/home.html'), name='home'),

     # ex : products/1/
    path('<int:product_id>/', views.search, name='search'),
   
    # ex: products/index/)
    path('index/', views.index, name='index'),

    # # ex: /products/5/
    path('<int:product_id>/', views.result, name='result'),
    
    # ex: /products/5/detail/
    path('<int:product_id>/detail/', views.detail, name='detail'),
]


# path('', views.index, name='index'),