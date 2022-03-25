from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from django.shortcuts import render
from django.views.generic import View
from products.models import Product
from products.forms import ProductForm
from django.utils.html import format_html
from appbbc.settings import CATEGORIES

from rest_framework import viewsets
from rest_framework import permissions
from products.serializers import ProductSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MyProducts(View):

    def get(self, request):
        products = Product.objects.filter(owner=request.user)
        cats = []
        for row in products:
            cats.append(dict(CATEGORIES)[str(row.category_bk)])
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
            'form_category': form.data['category_bk'],
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


# API
# Product List
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


# Product search
class ProductAPIView(generics.ListCreateAPIView):
    search_fields = ['description']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Product Update & Delete
class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProductSerializer(prod)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProductSerializer(prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        prod = self.get_object(pk)
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
