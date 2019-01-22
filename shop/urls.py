'''
Created: September 18, 2018
Created by: Ethan Lor
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor
		 November 27, 2018 Ethan Lor
		 December 8, 2018 Ethan Lor
'''

from django.urls import path
from . import views


# Main shop URL
app_name = 'shop'

# Shop URLs
urlpatterns = [
	path('', views.allProdCat, name = 'allProdCat'),
	path('<slug:c_slug>/', views.allProdCat, name = 'products_by_category'),
	path('<slug:c_slug>/<slug:product_slug>', views.ProdCatDetail, name = 'ProdCatDetail'),
]