'''
Created: September 18, 2018
Created by: Ethan Lor
Updated: December 8, 2018 Ethan Lor
'''

from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Get search results/products and render search page.
def searchResult(request):
	products = None
	query = None
	if 'q' in request.GET:
		query = request.GET.get('q')
		product_search = Product.objects.all().filter(Q(name__contains = query) | Q(description__contains = query))
		'''Paginator Code'''
		paginator = Paginator(product_search, 9)
		try:
			page = int(request.GET.get('page', '1'))
		except:
			page = 1
		try:
			products = paginator.page(page)
		except (EmptyPage, InvalidPage):
			products = paginator.page(paginator.num_pages)
	return render(request, 'search.html', {'query':query, 'products':products})

