from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "products"

urlpatterns = [
    # ex: /products/
    path('', TemplateView.as_view(template_name='products/home.html'), name='home'),
    # ex : /products/search/
    path('search/', views.search, name="search"),
]