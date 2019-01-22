'''
Created: September 18, 2018
Created by: Ethan Lor, Kala Arentz
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor, Kala Arentz
		 November 27, 2018 Ethan Lor
		 December 8, 2018 Ethan Lor
'''

from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required


# Render thank you page
def thanks(request, order_id):
	if order_id:
		customer_order = get_object_or_404(Order, id = order_id)
	return render(request, 'thanks.html', {'customer_order': customer_order})

# Get order history and render order history list page.
@login_required()
def orderHistory(request):
	if request.user.is_authenticated:
		user_id = request.user.id
		email = str(request.user.email)
		order_details = Order.objects.filter(user = user_id)
	return render(request, 'order/orders_list.html', {'order_details': order_details})

# Gets orders and render order detail page.
@login_required()
def viewOrder(request, order_id):
	if request.user.is_authenticated:
		email = str(request.user.email)
		order = Order.objects.get(id = order_id, emailAddress = email)
		order_items = OrderItem.objects.filter(order = order)
	return render(request, 'order/order_detail.html', {'order': order, 'order_items': order_items})
