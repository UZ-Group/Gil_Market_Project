from django.contrib import admin

from .models import ProductBrand


class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']

    class Meta:
        model = ProductBrand


admin.site.register(ProductBrand, ProductBrandAdmin)
