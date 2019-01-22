'''
Created: September 18, 2018
Created by: Ethan Lor, Benjamin Klipfel, Travis Waldvogel
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor, Benjamin Klipfel, Travis Waldvogel
		 November 27, 2018 Ethan Lor
		 December 8, 2018 Ethan Lor
'''

from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



# Model for Cart table.
class Cart(models.Model):
	cart_id = models.CharField(max_length = 250, blank = True)
	date_added = models.DateField(auto_now_add = True)

	class Meta:
		db_table = 'Cart'
		ordering = ['date_added']

	def __str__(self):
		return self.cart_id

# Model for CartItem table.
class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
	quantity = models.IntegerField()
	price = models.DecimalField(max_digits = 10, decimal_places = 2)
	code = models.CharField(max_length=50, blank = True)
	discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default = 0)
	discountPrice = models.DecimalField(max_digits = 10, decimal_places = 2)
	active = models.BooleanField(default = True)

	class Meta:
		db_table = 'CartItem'

	def sub_total(self):
		return self.discountPrice * self.quantity

	def __str__(self):
		return self.product

# Model for StateTax table.
class StateTax(models.Model):
	state = models.CharField(max_length=2, unique=True)
	tax = models.DecimalField(max_digits=5, decimal_places=2)

	class Meta:
		db_table = 'StateTax'
		ordering = ['state']
		verbose_name = 'state tax'
		verbose_name_plural = 'state taxes'

	def __str__(self):
		return self.state

# Model for BillingAddress table.
class BillingAddress(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	billingFirstName = models.CharField(max_length = 250, blank = True)
	billingLastName = models.CharField(max_length = 250, blank = True)
	billingAddress = models.CharField(max_length = 250, blank = True)
	billingCity = models.CharField(max_length = 250, blank = True)
	billingState = models.CharField(max_length = 5, blank = True)
	billingPostcode = models.CharField(max_length = 10, blank = True)
	billingCountry = models.CharField(max_length = 200, blank = True)

	class Meta:
		db_table = 'BillingAddress'
		ordering = ['user']
		verbose_name = 'Billing address'
		verbose_name_plural = 'Billing addresses'

# Model for ShippingAddress table.
class ShippingAddress(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	shippingFirstName = models.CharField(max_length = 250, blank = True)
	shippingLastName = models.CharField(max_length = 250, blank = True)
	shippingAddress = models.CharField(max_length = 250, blank = True)
	shippingCity = models.CharField(max_length = 250, blank = True)
	shippingState = models.CharField(max_length = 5, blank = True)
	shippingPostcode = models.CharField(max_length = 10, blank = True)
	shippingCountry = models.CharField(max_length = 200, blank = True)

	class Meta:
		db_table = 'ShippingAddress'
		ordering = ['user']
		verbose_name = 'Shipping address'
		verbose_name_plural = 'Shipping addresses'
