'''
Created: November 6, 2018
Created by: Ethan Lor
Updated: November 27, 2018 Ethan Lor
'''

from django.contrib import admin
from .models import StateTax


# Administartive configuration for StateTax model.
class StateTaxAdmin(admin.ModelAdmin):
	list_display = ['state', 'tax']
	search_fields = ['state']


admin.site.register(StateTax, StateTaxAdmin)
