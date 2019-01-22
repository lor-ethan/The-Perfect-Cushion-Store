'''
Created: September 18, 2018
Created by: Ethan Lor
'''

from django.contrib import admin
from .models import Order, OrderItem


# Administartive view for OrderItem
class OrderItemAdmin(admin.TabularInline):
	model = OrderItem
	fieldsets = [
	('Product',{'fields':['product'],}),
	('Quantity',{'fields':['quantity'],}),
	('Price',{'fields':['price'],}),
	]
	readonly_fields = ['product', 'quantity', 'price']
	can_delete = False
	max_num = 0
	template = 'admin/order/tabular.html'

# Administrative view for Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'billingName', 'emailAddress', 'created']
	list_display_links = ('id', 'billingName')
	serach_fields = ['id', 'billingName', 'emailAddress']
	readonly_fields = ['id', 'subtotal', 'shippingTotal', 'taxState', 'tax', 'taxAmount', 'total', 'user', 'emailAddress', 'created', 
						'billingName', 'billingAddress', 'billingCity', 'billingState', 'billingPostcode', 'billingCountry', 
						'shippingName', 'shippingAddress', 'shippingCity', 'shippingState','shippingPostcode', 'shippingCountry']

	fieldsets = [
	('ORDER INFORMATION', {'fields': ['id', 'subtotal', 'shippingTotal', 'taxState', 'tax', 'taxAmount', 'total', 'created']}),
	('BILLING INFORMATION', {'fields': ['billingName', 'billingAddress', 'billingCity', 'billingState', 'billingPostcode', 'billingCountry', 'emailAddress']}),
	('SHIPPING INFORMATION', {'fields': ['shippingName', 'shippingAddress', 'shippingCity', 'shippingState', 'shippingPostcode', 'shippingCountry']}),
	]

	inlines = [
		OrderItemAdmin,
	]

	search_fields = ['id', 'billingName', 'emailAddress']

	def has_delete_permission(self, request, obj = None):
		return False

	def has_add_permission(self, request):
		return False
