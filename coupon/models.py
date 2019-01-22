'''
Created: September 18, 2018
Created by: Ethan Lor, Benjamin Klipfel, Travis Waldvogel
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor, Benjamin Klipfel, Travis Waldvogel
'''

from django.db import models
from shop.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator


# Model for Coupon table
class Coupon(models.Model):
	code = models.CharField(max_length=50, unique=True)
	valid_from = models.DateTimeField()
	valid_to = models.DateTimeField()
	discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	active = models.BooleanField()

	class Meta:
		db_table = 'Coupon'

	def __str__(self):
		return self.code
