'''
Created: September 18, 2018
Created by: Ethan Lor
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor
		 November 27, 2018 Ethan Lor
'''

from django.urls import path
from .import views


# Cart application name.
app_name = 'cart'

# Cart URLs.
urlpatterns = [
	path('add/<int:product_id>/', views.add_cart, name = 'add_cart'),
	path('', views.cart_detail, name = 'cart_detail'),
	path('remove/<int:product_id>', views.cart_remove, name = 'cart_remove'),
	path('full_remove/<int:product_id>', views.full_remove, name = 'full_remove'),
	path('cancel_order/', views.cancel_order, name = 'cancel_order'),
	path('checkout/', views.checkout, name = 'checkout'),
	path('address/', views.save_info, name = 'save_info'),
	path('payment/', views.payment, name = 'payment'),
	path('order/', views.processOrder, name = 'process'),
]