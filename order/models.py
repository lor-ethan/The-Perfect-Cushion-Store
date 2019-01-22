'''
Created: September 18, 2018
Created by: Ethan Lor, Benjamin Klipfel, Travis Waldvogel
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor, Benjamin Klipfel, Travis Waldvogel
'''

from django.db import models


# Model for Order table
class Order(models.Model):
	subtotal = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True,verbose_name = 'Subtotal')
	shippingTotal = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True,verbose_name = 'Shipping Total')
	taxState = models.CharField(max_length=2, blank = True,verbose_name = 'Tax State')
	tax = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True,verbose_name = 'Tax')
	taxAmount = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True,verbose_name = 'Tax Amount')
	total = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True,verbose_name = 'Total')
	user = models.CharField(max_length = 250, blank = True, null = True)
	emailAddress = models.EmailField(max_length = 250, blank = True, verbose_name = 'Email Address')
	created = models.DateTimeField(auto_now_add = True)
	billingName = models.CharField(max_length = 250, blank = True)
	billingAddress = models.CharField(max_length = 250, blank = True)
	billingCity = models.CharField(max_length = 250, blank = True)
	billingState = models.CharField(max_length = 5, blank = True)
	billingPostcode = models.CharField(max_length = 10, blank = True)
	billingCountry = models.CharField(max_length = 200, blank = True)
	shippingName = models.CharField(max_length = 250, blank = True)
	shippingAddress = models.CharField(max_length = 250, blank = True)
	shippingCity = models.CharField(max_length = 250, blank = True)
	shippingState = models.CharField(max_length = 5, blank = True)
	shippingPostcode = models.CharField(max_length = 10, blank = True)
	shippingCountry = models.CharField(max_length = 200, blank = True)

	class Meta:
		db_table = 'Order'
		ordering = ['-created']

	def __str__(self):
		return str(self.id)


# Model for OrderItem table
class OrderItem(models.Model):
	product = models.CharField(max_length = 250)
	quantity = models.IntegerField()
	price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'USD Price')
	order = models.ForeignKey(Order, on_delete = models.CASCADE)

	class Meta:
		db_table = 'OrderItem'

	def sub_total(self):
		return self.quantity * self.price

	def __str__(self):
		return self.product
