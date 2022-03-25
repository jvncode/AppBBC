from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category_bk', 'description', 'functionality', 'image', 'location']
        list_display = ['category']
        exclude = []
