from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "products"

urlpatterns = [
    # ex : /products/search/
    path('search/', views.search, name="search"),
    path('<int:product_id>/detail/', views.detail, name='detail'),
]
#     path('detail/<int:product.id>/', views.detail, name="detail"),
# ] 