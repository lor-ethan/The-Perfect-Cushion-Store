'''
Created: September 18, 2018
Created by: Ethan Lor
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor
'''

from django.contrib import admin
from .models import Coupon


# Administrative configuration for Coupon
class CouponAdmin(admin.ModelAdmin):
	list_display = ['code', 'valid_from', 'valid_to', 'discount', 'product', 'active']
	list_filter = ['active', 'valid_from', 'valid_to']
	search_fields = ['code']


admin.site.register(Coupon, CouponAdmin)
