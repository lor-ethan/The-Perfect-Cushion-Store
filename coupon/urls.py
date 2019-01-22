'''
Created: September 18, 2018
Created by: Ethan Lor
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor
'''

from django.urls import path
from .import views

# Coupon application name.
app_name = 'coupon'

# Coupon URLs
urlpatterns = [
	path('apply/', views.coupon_apply, name='apply')
]