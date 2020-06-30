from django.shortcuts import render, redirect
from django.views.generic import View
from products.models import Product
from products.forms import ProductForm

class MyProducts(View):
    
    def get(self, request):
        products = Product.objects.all()
        
        context = {
            'products_list': products,
        }
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
        
        form = ProductForm(request.POST, instance=product_with_owner)
        if form.is_valid():
            new_product = form.save()
            form = ProductForm()
            success_message = '¡Producto publicado con éxito!'
        context = {
            'form': form,
            'success_message': success_message,
        }
        return render(request, 'products/newProduct.html', context)
    

class SearchProduct(View):
    def get(self, request):
        return render(request, 'products/searchProduct.html')

    def post(self, request):
        q = request.POST.get('BusquedaSet')
        if q != '':
            products = Product.objects.filter(description__icontains=q)
        else:
            products = None
        return render(request, 'products/searchProduct.html', {'products': products})

