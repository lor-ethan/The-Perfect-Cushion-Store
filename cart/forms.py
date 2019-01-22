'''
Created: September 18, 2018
Created by: Ethan Lor
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor
		 November 27, 2018 Ethan Lor
		 December 8, 2018 Ethan Lor
'''

from django import forms
import datetime


# State choices for billing and shipping forms.
states = [
	('',''),
    ('AL', 'AL (Alabama)'), ('AK', 'AK (Alaska)'), ('AZ', 'AZ (Arizona)'), ('AR', 'AR (Arkansas)'), ('CA', 'CA (California)'),
    ('CO', 'CO (Colorado)'), ('CT', 'CT (Connecticut)'), ('DC', 'DC (District Of Columbia)'), ('DE', 'DE (Delaware)'),
    ('FL', 'FL (Florida)'), ('GA', 'GA (Georgia)'), ('HI', 'HI (Hawaii)'), ('ID', 'ID (Idaho)'), ('IL', 'IL (Illinois)'),
	('IN', 'IN (Indiana)'), ('IA', 'IA (Iowa)'), ('KS', 'KS (Kansas)'), ('KY', 'KY (Kentucky)'), ('LA', 'LA (Louisiana)'),
	('ME', 'ME (Maine)'), ('MD', 'MD (Maryland)'), ('MA', 'MA (Massachusetts)'), ('MI', 'MI (Michigan)'), ('MN', 'MN (Minnesota)'),
	('MS', 'MS (Mississippi)'), ('MO', 'MO (Missouri)'), ('MT', 'MT (Montana)'), ('NE', 'NE (Nebraska)'), ('NV', 'NV (Nevada)'), 
	('NH', 'NH (New Hampshire)'), ('NJ', 'NJ (New Jersey )'), ('NM', 'NM (New Mexico)'), ('NY', 'NY (New York)'), ('NC', 'NC (North Carolina)'), 
	('ND', 'ND (North Dakota)'), ('OH', 'OH (Ohio)'), ('OK', 'OK (Oklahoma)'), ('OR', 'OR (Oregon)'), ('PA', 'PA (Pennsylvania)'), 
	('RI', 'RI (Rhode Island)'), ('SC', 'SC (South Carolina)'), ('SD', 'SD (South Dakota)'), ('TN', 'TN (Tennessee)'), ('TX', 'TX (Texas)'),
	('UT', 'UT (Utah)'), ('VT', 'VT (Vermont)'), ('VA', 'VA (Virginia)'), ('WA', 'WA (Washington)'),('WV', 'WV (West Virginia)'),
	('WI', 'WI (Wisconsin)'),('WY', 'WY (Wyoming)')
    ]

# Edit billing form.
class BillingForm(forms.Form):
	email = forms.EmailField(max_length = 254, help_text = 'eg. youremail@anyemail.com')
	billing_first_name = forms.CharField(max_length = 250, required = True)
	billing_last_name = forms.CharField(max_length = 250, required = True)
	billing_address = forms.CharField(max_length = 100, required = True)
	billing_city = forms.CharField(max_length = 250, required = True)
	billing_state = forms.CharField(widget=forms.Select(choices=states))
	billing_zip_code = forms.CharField(max_length = 10, required = True)

# Edit shipping form
class ShippingForm(forms.Form):
	shipping_first_name = forms.CharField(max_length = 250, required = True)
	shipping_last_name = forms.CharField(max_length = 250, required = True)
	shipping_address = forms.CharField(max_length = 100, required = True)
	shipping_city = forms.CharField(max_length = 250, required = True)
	shipping_state = forms.CharField(widget=forms.Select(choices=states))
	shipping_zip_code = forms.CharField(max_length = 10, required = True)
 
# Edit payment form.
class PaymentForm(forms.Form):
  number = forms.CharField(required = True, label = "Card Number", min_length = 15, max_length = 16)
  first_name = forms.CharField(required=True, label="Card Holder First Name", max_length=30)
  last_name = forms.CharField(required=True, label="Card Holder Last Name", max_length=30)
  expiration_month = forms.ChoiceField(required=True, choices=[(x, x) for x in range(1, 13)])
  expiration_year = forms.ChoiceField(required=True, choices=[(x, x) for x in range(datetime.date.today().year, datetime.date.today().year + 15)])
  cvv_number = forms.CharField(required = True, label = "CVV Number", min_length = 3, max_length = 3)

# Edit Billing form.
class EditBillingForm(forms.Form):
	billing_first_name = forms.CharField(max_length = 250, required = True)
	billing_last_name = forms.CharField(max_length = 250, required = True)
	billing_address = forms.CharField(max_length = 100, required = True)
	billing_city = forms.CharField(max_length = 250, required = True)
	billing_state = forms.CharField(widget=forms.Select(choices=states))
	billing_zip_code = forms.CharField(max_length = 10, required = True)

# Edit Shipping form.
class EditShippingForm(forms.Form):
	shipping_first_name = forms.CharField(max_length = 250, required = True)
	shipping_last_name = forms.CharField(max_length = 250, required = True)
	shipping_address = forms.CharField(max_length = 100, required = True)
	shipping_city = forms.CharField(max_length = 250, required = True)
	shipping_state = forms.CharField(widget=forms.Select(choices=states))
	shipping_zip_code = forms.CharField(max_length = 10, required = True)
