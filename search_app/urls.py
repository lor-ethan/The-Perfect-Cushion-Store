'''
Created: September 18, 2018
Created by: Ethan Lor
'''

from django.urls import path
from . import views

# Search Application name
app_name = 'search_app'

# Search URL patterns
urlpatterns = [
	path('', views.searchResult, name = 'searchResult'),
]