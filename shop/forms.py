'''
Created: September 18, 2018
Created by: Ethan Lor
Updated: October 25, 2018 Ethan Lor
		 November 6, 2018 Ethan Lor
		 November 27, 2018 Ethan Lor
		 December 8, 2018 Ethan Lor
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Signup Form
class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length = 100, required = True)
	last_name = forms.CharField(max_length = 100, required = True)
	email = forms.EmailField(max_length = 254, help_text = 'eg. youremail@anyemail.com')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.pop('autofocus')

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

# Edit user form
class EditUserForm(forms.Form):
	first_name = forms.CharField(max_length = 100, required = True)
	last_name = forms.CharField(max_length = 100, required = True)
	email = forms.EmailField(max_length = 254, help_text = 'eg. youremail@anyemail.com')