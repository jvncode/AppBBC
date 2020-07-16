from django.contrib import admin
from products.models import Product
from django.utils.html import format_html


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'category',
        'description',
        'image',
        'foto', 
        'location'
    )

    def foto (self, obj):
        return format_html('<img src=/media/{} width="130" height="100"/>', obj.image)
admin.site.register(Product, PersonAdmin)

