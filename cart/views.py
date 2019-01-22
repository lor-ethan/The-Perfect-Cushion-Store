'''
Created: September 18, 2018
Created by: Ethan Lor, Kala Arentz
Updated: October 25, 2018 Ethan Lor, Kala Arentz
		 November 6, 2018 Ethan Lor, Kala Arentz
		 November 27, 2018 Ethan Lor, Kala Arentz
		 December 8, 2018 Ethan Lor
'''

from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Cart, CartItem, StateTax, BillingAddress, ShippingAddress
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.conf import settings
from order.models import Order, OrderItem
from decimal import Decimal
from coupon.models import Coupon
from coupon.forms import CouponApplyForm
from .forms import BillingForm, ShippingForm, PaymentForm
from django.views.decorators.http import require_POST
import datetime
from django.contrib import messages


# Get cart or create a new cart.
def _cart_id(request):
	cart = request.session.session_key
	if not cart:
		cart = request.session.create()
	return cart

# Add item to cart or increment item in cart by one. Redirect to cart detail page.
def add_cart(request, product_id):
	product = Product.objects.get(id = product_id)
	try:
		cart = Cart.objects.get(cart_id = _cart_id(request))
	except Cart.DoesNotExist:
		cart = Cart.objects.create(
				cart_id = _cart_id(request)
			)
		cart.save()
	try:
		cart_item = CartItem.objects.get(product = product, cart = cart)
		if cart_item.quantity < cart_item.product.stock:
			cart_item.quantity += 1
		cart_item.save()
	except CartItem.DoesNotExist:
		cart_item = CartItem.objects.create(
				product = product,
				quantity = 1,
				price = product.price,
				discountPrice = product.price,
				cart = cart
			)
		cart_item.save()
	return redirect('cart:cart_detail')

# Get all items in cart and render cart page.
def cart_detail(request, total = 0, counter = 0, cart_items = None, subtotal = 0):
	coupon_apply_form = CouponApplyForm()

	try:
		cart = Cart.objects.get(cart_id = _cart_id(request))
		cart_items = CartItem.objects.filter(cart = cart, active = True)
		for cart_item in cart_items:
			total += (cart_item.discountPrice * cart_item.quantity)
			counter += cart_item.quantity
	except ObjectDoesNotExist:
		pass

	subtotal = total
	request.session['subtotal'] = str(subtotal)

	return render(request, 'cart.html', dict(cart_items = cart_items, total = total, counter = counter, subtotal = subtotal, coupon_apply_form = coupon_apply_form))

# Remove one of selected product. If zero left, delete product from cart. Redirect to cart detail page.
def cart_remove(request, product_id):
	cart = Cart.objects.get(cart_id = _cart_id(request))
	product = get_object_or_404(Product, id = product_id)
	cart_item = CartItem.objects.get(product = product, cart = cart)
	if cart_item.quantity > 1:
		cart_item.quantity -= 1
		cart_item.save()
	else:
		cart_item.delete()
	return redirect('cart:cart_detail')

# Remove all quantities of a product from cart. Redirect to cart detials.
def full_remove(request, product_id):
	cart = Cart.objects.get(cart_id = _cart_id(request))
	product = get_object_or_404(Product, id = product_id)
	cart_item = CartItem.objects.get(product = product, cart = cart)
	cart_item.delete()
	return redirect('cart:cart_detail')

# Cancel order and delete all order items. Redirect to cart details.
def cancel_order(request):
	try:
		cart = Cart.objects.get(cart_id = _cart_id(request))
		cart_items = CartItem.objects.filter(cart = cart, active = True)
		for cart_item in cart_items:
			cart_item.delete()
	except ObjectDoesNotExist:
		pass
	return redirect('cart:cart_detail')

# Get user information and render checkout page.
def checkout(request, subtotal = 0):
	billing_form = BillingForm()
	shipping_form = ShippingForm()
	current_user = request.user
	user_email = None
	if current_user.id:
		user_id	= current_user.id
		user_email = current_user.email
		try:
			billing_address = BillingAddress.objects.get(user=current_user)
			billing_form = BillingForm(initial = {
									'email': current_user.email,
									'billing_first_name': billing_address.billingFirstName,
									'billing_last_name': billing_address.billingLastName,
									'billing_address': billing_address.billingAddress,
									'billing_city': billing_address.billingCity,
									'billing_state': billing_address.billingState,
									'billing_zip_code': billing_address.billingPostcode,
									})
			try:
				shipping_address = ShippingAddress.objects.get(user=current_user)
				shipping_form = ShippingForm(initial = {
									'shipping_first_name': shipping_address.shippingFirstName,
									'shipping_last_name': shipping_address.shippingLastName,
									'shipping_address': shipping_address.shippingAddress,
									'shipping_city': shipping_address.shippingCity,
									'shipping_state': shipping_address.shippingState,
									'shipping_zip_code': shipping_address.shippingPostcode,
									})
			except ShippingAddress.DoesNotExist:
				pass
		except BillingAddress.DoesNotExist:
			billing_form = BillingForm(initial = {
									'email': current_user.email,
									'billing_first_name': current_user.first_name,
									'billing_last_name': current_user.last_name,
									})

	subtotal = Decimal(request.session['subtotal'])
	shippingTotal = subtotal + Decimal('5.99')
	request.session['shippingTotal'] = str(shippingTotal)

	return render(request, 'checkout.html', dict(subtotal = subtotal, shippingTotal = shippingTotal, billing_form = billing_form, shipping_form = shipping_form))

# Validates user information being updated from checkout page and redirects back to check out page.
@require_POST
def save_info(request):
	if request.POST.get("save"):
		if request.POST.get('same_addresses'):
			billing_address, created = BillingAddress.objects.update_or_create(
        		user=request.user, defaults={
        									'billingFirstName': request.POST['billing_first_name'],
        									'billingLastName': request.POST['billing_last_name'],
        									'billingAddress': request.POST['billing_address'],
        									'billingCity': request.POST['billing_city'],
        									'billingState': request.POST['billing_state'],
        									'billingPostcode': request.POST['billing_zip_code'],
        									'billingCountry': "US",
        									}
				)
			return redirect('cart:checkout')
		else:
			billing_address, created = BillingAddress.objects.update_or_create(
        		user=request.user, defaults={
        									'billingFirstName': request.POST['billing_first_name'],
        									'billingLastName': request.POST['billing_last_name'],
        									'billingAddress': request.POST['billing_address'],
        									'billingCity': request.POST['billing_city'],
        									'billingState': request.POST['billing_state'],
        									'billingPostcode': request.POST['billing_zip_code'],
        									'billingCountry': "US",
        									}
				)

			shipping_address, created = ShippingAddress.objects.update_or_create(
        		user=request.user, defaults={
        									'shippingFirstName': request.POST['shipping_first_name'],
        									'shippingLastName': request.POST['shipping_last_name'],
        									'shippingAddress': request.POST['shipping_address'],
        									'shippingCity': request.POST['shipping_city'],
        									'shippingState': request.POST['shipping_state'],
        									'shippingPostcode': request.POST['shipping_zip_code'],
        									'shippingCountry': "US",
        									}
        		)
			return redirect('cart:checkout')
	elif request.POST.get("tax"):
		if request.POST.get('same_addresses'):
			billing = dict(
					firstName = request.POST['billing_first_name'],
        			lastName = request.POST['billing_last_name'],
        			address = request.POST['billing_address'],
        			city = request.POST['billing_city'],
        			state = request.POST['billing_state'],
        			postcode = request.POST['billing_zip_code'],
        			country = "US",
				)
			shipping = dict(
					firstName = request.POST['billing_first_name'],
        			lastName = request.POST['billing_last_name'],
        			address = request.POST['billing_address'],
        			city = request.POST['billing_city'],
        			state = request.POST['billing_state'],
        			postcode = request.POST['billing_zip_code'],
        			country = "US",
				)

			request.session['email'] = request.POST['email'] 
			request.session['billing'] = billing
			request.session['shipping'] = shipping
			state = StateTax.objects.get(state = billing['state'])
			tax = state.tax
			tax_amount = round(tax / Decimal('100') * Decimal(request.session['shippingTotal']), 2)
			total = Decimal(request.session['shippingTotal']) + tax_amount
			request.session['state'] = state.state
			request.session['tax'] = str(tax)
			request.session['taxAmount'] = str(tax_amount)
			request.session['total'] = str(total)

			return redirect('cart:payment')
		else:
			billing = dict(
					firstName = request.POST['billing_first_name'],
        			lastName = request.POST['billing_last_name'],
        			address = request.POST['billing_address'],
        			city = request.POST['billing_city'],
        			state = request.POST['billing_state'],
        			postcode = request.POST['billing_zip_code'],
        			country = "US",
				)
			shipping = dict(
					firstName = request.POST['shipping_first_name'],
        			lastName = request.POST['shipping_last_name'],
        			address = request.POST['shipping_address'],
        			city = request.POST['shipping_city'],
        			state = request.POST['shipping_state'],
        			postcode = request.POST['shipping_zip_code'],
        			country = "US",
				)

			request.session['email'] = request.POST['email']
			request.session['billing'] = billing
			request.session['shipping'] = shipping
			state = StateTax.objects.get(state = billing['state'])
			tax = state.tax
			tax_amount = round(tax / Decimal('100') * Decimal(request.session['shippingTotal']), 2)
			total = Decimal(request.session['shippingTotal']) + tax_amount
			request.session['state'] = state.state
			request.session['tax'] = str(tax)
			request.session['taxAmount'] = str(tax_amount)
			request.session['total'] = str(total)

			return redirect('cart:payment')

# Process payment and redirect to payment or process function. Render payment page if not a POST.
def payment(request):
	if request.method == "POST":
		print(datetime.date.today().month)
		if int(request.POST['expiration_year']) == int(datetime.date.today().year) and int(request.POST['expiration_month']) < int(datetime.date.today().month):
			messages.error(request, 'Card entered is expired. Please enter a valid card.')
			print("expired")
			return redirect('cart:payment')
		else:
			return redirect('cart:process')

	return render(request, 'payment.html', dict(payment_form = PaymentForm))

# Process order and save order details. Redirect to thank you page.
def processOrder(request):
	print("process order")
	print(request.session['billing'])
	print(request.session['billing']['firstName'])
	order_details = Order.objects.create(
			subtotal = Decimal(request.session['subtotal']),
			shippingTotal = Decimal(request.session['shippingTotal']),
			taxState = request.session['state'],
			tax = request.session['tax'],
			taxAmount = Decimal(request.session['taxAmount']),
			total = Decimal(request.session['total']),
			user = request.user.id,
			emailAddress = request.session['email'], 
			billingName = request.session['billing']['firstName'] + ' ' + request.session['billing']['lastName'],
			billingAddress = request.session['billing']['address'],
			billingCity = request.session['billing']['city'],
			billingState = request.session['billing']['state'],
			billingPostcode = request.session['billing']['postcode'],
			billingCountry = "US",
			shippingName = request.session['shipping']['firstName'] + ' ' + request.session['shipping']['lastName'],
			shippingAddress = request.session['shipping']['address'],
			shippingCity = request.session['shipping']['city'],
			shippingState = request.session['shipping']['state'],
			shippingPostcode = request.session['shipping']['postcode'],
			shippingCountry = "US",
		)
	order_details.save()
	cart = Cart.objects.get(cart_id = _cart_id(request))
	cart_items = CartItem.objects.filter(cart = cart, active = True)
	for order_item in cart_items:
		oi = OrderItem.objects.create(
				product = order_item.product.name,
				quantity = order_item.quantity,
				price = order_item.discountPrice,
				order = order_details
			)
		oi.save()
	'''Reduce stock when order is placed or saved'''
	products = Product.objects.get(id = order_item.product.id)
	products.stock = int(order_item.product.stock - order_item.quantity)
	products.save()
	order_item.delete()
	'''The terminal will print this message when the order is saved'''
	return redirect('order:thanks', order_details.id)

