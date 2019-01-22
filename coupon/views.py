'''
Created: September 18, 2018
Created by: Ethan Lor, Kala Arentz
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Kala Arentz
		 November 27, 2018 Ethan Lor
		 December 8, 2018 Ethan Lor
'''

from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Coupon
from cart.models import Cart, CartItem
from .forms import CouponApplyForm
from django.views.decorators.http import require_POST
from decimal import Decimal


# Verify coupon and apply coupon. Redirect to cart details page.
@require_POST
def coupon_apply(request):
	now = timezone.now()
	form = CouponApplyForm(request.POST)
	if form.is_valid():
		print(now)
		code = form.cleaned_data['Promotion_code']
		try:
			coupon = Coupon.objects.get(code__iexact=code,
										valid_from__lte=now,
										valid_to__gte=now,
										active=True)
			print(coupon.valid_from)
			print(coupon.valid_to)
			cart_id = request.session.session_key
			try:
				cart = Cart.objects.get(cart_id = cart_id)
				try:
					cart_item = CartItem.objects.get(cart = cart, product_id = coupon.product_id)
					cart_item.code = coupon.code
					cart_item.discount = coupon.discount
					cart_item.discountPrice = cart_item.price - round(coupon.discount / Decimal('100') * cart_item.price, 2)
					cart_item.save()
				except CartItem.DoesNotExist:
					print('CartItem Does Not Exist')
					messages.error(request, 'Promotion Code: ' + code + ', not applicable to items in cart')
			except Cart.DoesNotExist:
				print('Cart Does Not Exist')
		except Coupon.DoesNotExist:
			print("Coupon Does Not Exist")
			messages.error(request, 'Invalid Promotion Code: ' + code)
			
	return redirect('cart:cart_detail') 
