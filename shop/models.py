'''
Created: September 18, 2018
Created by: Ethan Lor, Benjamin Klipfel, Travis Waldvogel
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor, Benjamin Klipfel, Travis Waldvogel
		 November 27, 2018 Ethan Lor
		 December 8, 2018 Ethan Lor
'''

from django.db import models
from django.urls import reverse

# Database model for Category table
class Category(models.Model):
	name = models.CharField(max_length = 250, unique = True)
	slug = models.SlugField(max_length = 250, unique = True)
	description = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'category', blank = True)

	class Meta:
		db_table = 'Category'
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self):
		return reverse('shop:products_by_category', args = [self.slug])

	def __str__(self):
		return '{}'.format(self.name)

# Database model for Product table
class Product(models.Model):
	name = models.CharField(max_length = 250, unique = True)
	slug = models.SlugField(max_length = 250, unique = True)
	description = models.TextField(blank = True)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	price = models.DecimalField(max_digits = 10, decimal_places = 2)
	image = models.ImageField(upload_to = 'product', blank = True)
	stock = models.IntegerField()
	available = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = 'Product'
		ordering = ('name',)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('shop:ProdCatDetail', args = [self.category.slug, self.slug])

	def __str__(self):
		return '{}'.format(self.name)
