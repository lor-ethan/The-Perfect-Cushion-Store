'''
Created: September 18, 2018
Created by: Ethan Lor
'''

from .models import Category


# Administrative menu for Category
def menu_links(request):
	links = Category.objects.all()
	return dict(links = links)
	