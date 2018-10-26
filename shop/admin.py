from django.contrib import admin
# from .forms import SignUpForm
from .models import Category, Product


# admin.site.register(SignUpForm)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}
	search_fields = ['name']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
	list_editable = ['price', 'stock', 'available']
	prepopulated_fields = {'slug':('name',)}
	search_fields = ['name']
	list_per_page = 20
admin.site.register(Product, ProductAdmin)