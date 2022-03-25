from django.urls import path
from products.views import MyProducts, CreateProduct, SearchProduct, ProductOk, ProductCard

urlpatterns = [
    path('myProducts', MyProducts.as_view(), name='my_products'),
    path('newProduct', CreateProduct.as_view(), name='new_product'),
    path('newProductOk', ProductOk.as_view(), name='product_ok'),
    path('searchProduct', SearchProduct.as_view(), name='search_product'),
    path('productCard', ProductCard.as_view(), name='product_card'),
]
