from django.contrib import admin
from products.models import Product, Category
from django.utils.html import format_html


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'category_bk',
        'description',
        'image',
        'foto',
        'location'
    )
    fields = (
        'owner',
        'category_bk',
        'description',
        'image',
        'foto',
        'location'
    )

    def foto (self, obj):
        return format_html('<img src=/media/{} width="130" height="100"/>', obj.image)


class CatAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = (
        'title',
        'slug',
        'is_active',
        'link_products'
    )
    fields = (
        'title',
        'slug',
        'is_active',
    )
    list_filter = ('is_active', 'title')
    list_editable = ['is_active']

    def link_products(self, obj):
        result = Product.objects.filter(category_bk=obj)
        return len(result)

admin.site.register(Product, PersonAdmin)
admin.site.register(Category, CatAdmin)

