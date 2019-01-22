'''
Created: September 18, 2018
Created by: Ethan Lor
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor
		 November 27, 2018 Ethan Lor
		 December 8, 2018 Ethan Lor
'''

from django.urls import path
from .import views

# Order application name
app_name = 'order'

# Order URLs
urlpatterns = [
	path('thanks/<int:order_id>', views.thanks, name = 'thanks'),
	path('history/', views.orderHistory, name = 'order_history'),
	path('<int:order_id>/', views.viewOrder, name = 'order_detail'),
] 