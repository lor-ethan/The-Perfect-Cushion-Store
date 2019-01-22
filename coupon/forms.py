'''
Created: September 18, 2018
Created by: Ethan Lor
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor
'''

from django import forms


# Coupon form
class CouponApplyForm(forms.Form):
	Promotion_code = forms.CharField()