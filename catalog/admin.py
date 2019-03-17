from django.contrib import admin
from .models import Category, Product
# Register your models here.

#modelos para o catalogo
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

#modelos para os Produtos
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
