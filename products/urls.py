from django.urls import path
from products import views
from products.views import MyProducts, CreateProduct

urlpatterns = [
    path('myProducts', MyProducts.as_view(), name='my_products'),
    path('newProduct', CreateProduct.as_view(), name='new_product'),
]