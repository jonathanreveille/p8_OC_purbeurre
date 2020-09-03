from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name="index"),
#     path('results/', views.results, name="results"),
#     path('favorites/', views.favorites, name="favorites"),
# ]


urlpatterns = [
    # ex: /products/
    path('', views.index, name='index'),
    # ex: /products/5/
    path('<int:product_id>/', views.result, name='result'),
    # ex: /products/5/details/
    path('<int:product_id>/details/', views.details, name='details'),
]