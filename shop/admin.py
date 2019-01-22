'''
Created: September 18, 2018
Created by: Ethan Lor
'''

from django.contrib import admin
from .models import Category, Product


# Administrative view for Category
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}
	search_fields = ['name']
admin.site.register(Category, CategoryAdmin)

# Administrative view for Product
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
	list_editable = ['price', 'stock', 'available']
	prepopulated_fields = {'slug':('name',)}
	search_fields = ['name']
	list_per_page = 20
admin.site.register(Product, ProductAdmin)
