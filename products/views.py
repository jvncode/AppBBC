from django.shortcuts import render, redirect
from django.views.generic import View
from products.models import Product
from products.forms import ProductForm
from django.conf import settings
from django.utils.html import format_html
from appbbc.settings import CATEGORIES, FUNCTIONALITIES




class MyProducts(View):

    def get(self, request):
        products = Product.objects.filter(owner=request.user)
        cats = []
        for row in products:
            cats.append(dict(CATEGORIES)[row.category])
        context = {
            'products_list': products,
            'cats': cats,
        }
        print(context)
        return render(request, 'products/myProducts.html', context)

class CreateProduct(View):
    def get(self, request):
        form = ProductForm()
        success_message = ''
        context = {
            'form': form,
            'success_message': success_message,
        }
        return render(request, 'products/newProduct.html', context)
    
        
    def post(self, request):
        
        success_message = ''
        product_with_owner = Product()
        product_with_owner.owner = request.user
        
        form = ProductForm(request.POST, request.FILES, instance=product_with_owner)
        if form.is_valid():
            form.save()
            success_message = '¡Producto publicado con éxito!'
        context = {
            'form_category': form.data['category'],
            'form_description': form.data['description'],
            'form_functionality': form.data['functionality'],
            'form_image': format_html('<img src=/media/{}/{} width="230" height="200"/>'.format(request.user, request.FILES['image'])),
            'form_location': form.data['location'],
            'success_message': success_message,
        }
        return render(request, 'products/newProductOk.html', context)
    
class ProductOk(View):
    pass

class SearchProduct(View):
    def get(self, request):
        return render(request, 'products/searchProduct.html')

    def post(self, request):
        q = request.POST.get('BusquedaSet')
        if q != '':
            products = Product.objects.filter(description__icontains=q)
            context = {
                'products': products,
            }
        else:
            products = None
            context = {
                'products': products,
            }
        return render(request, 'products/searchProduct.html', context)


class ProductCard(View):
    def get(self, request):
        return render(request, 'products/productCard.html')
