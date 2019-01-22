'''
Created: September 18, 2018
Created by: Ethan Lor, Kala Arentz
Updated: October 25, 2018 Ethan Lor, Kala Arentz
		 November 6, 2018 Ethan Lor, Kala Arentz
		 November 27, 2018 Ethan Lor, Kala Arentz
		 December 8, 2018 Ethan Lor
'''

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Product
from cart.models import BillingAddress, ShippingAddress
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, User
from .forms import SignUpForm, EditUserForm
from cart.forms import EditBillingForm, EditShippingForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages


# Returns Test Index Page.
def index(request):
	text_var = 'This is my first django app web page.'
	return HttpResponse(text_var)

# Finds all products, creates pagination, and renders shop page.
def allProdCat(request, c_slug = None):
	c_page = None
	products_list = None
	if c_slug != None:
		c_page = get_object_or_404(Category,slug = c_slug)
		products_list = Product.objects.filter(category = c_page, available = True)
	else:
		products_list = Product.objects.all().filter(available = True)
	'''Paginator Code'''
	paginator = Paginator(products_list, 9)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1
	try:
		products = paginator.page(page)
	except (EmptyPage, InvalidPage):
		products = paginator.page(paginator.num_pages)
	return render(request, 'shop/category.html', {'category':c_page, 'products':products})
	
# Finds product deatils and renders product details page.
def ProdCatDetail(request, c_slug, product_slug):
	try:
		product = Product.objects.get(category__slug = c_slug, slug = product_slug)
	except Exception as e:
		raise e
	return render(request, 'shop/product.html', {'product':product})

# Finds user manual and renders user manual page.
def manual(request):
	image_data = open('static/media/UserManual.pdf', 'rb').read()
	return HttpResponse(image_data, content_type='application/pdf')

# Validates signup form and renders signup page.
def signupView(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			signup_user = User.objects.get(username = username)
			customer_group = Group.objects.get(name = 'Customer')
			customer_group.user_set.add(signup_user)
	else:
		form = SignUpForm()
	return render(request, 'accounts/signup.html', {'form':form})

# Validates signin form and renders signin page.
def signinView(request):
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username = username, password = password)
			if user is not None:
				login(request, user)
				return redirect('shop:allProdCat')
			else:
				return redirect('signup')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/signin.html', {'form':form})

# Sign outs user and redirects to signin page.
def signoutView(request):
	logout(request)
	return redirect('signin')

# Renders edit profile page.
@login_required()
def edit(request):
	user_form = EditUserForm(initial = {
				'first_name':request.user.first_name,
				'last_name': request.user.last_name,
				'email': request.user.email
		})

	billing_form = EditBillingForm()
	try:
		billing_address = BillingAddress.objects.get(user=request.user)
		billing_form = EditBillingForm(initial = {
									'billing_first_name': billing_address.billingFirstName,
									'billing_last_name': billing_address.billingLastName,
									'billing_address': billing_address.billingAddress,
									'billing_city': billing_address.billingCity,
									'billing_state': billing_address.billingState,
									'billing_zip_code': billing_address.billingPostcode,
									})
	except BillingAddress.DoesNotExist:
		print("Billing Address Does Not Exist")

	shipping_form = EditShippingForm()
	try:
		shipping_address = ShippingAddress.objects.get(user=request.user)
		shipping_form = EditShippingForm(initial = {
									'shipping_first_name': shipping_address.shippingFirstName,
									'shipping_last_name': shipping_address.shippingLastName,
									'shipping_address': shipping_address.shippingAddress,
									'shipping_city': shipping_address.shippingCity,
									'shipping_state': shipping_address.shippingState,
									'shipping_zip_code': shipping_address.shippingPostcode,
									})
	except ShippingAddress.DoesNotExist:
		print("Shipping Address Does Not Exist")

	return render(request, 'accounts/edit.html', {'user_form':user_form, 'billing_form':billing_form, 'shipping_form':shipping_form})

# Validates user form and updates user information. Redirect to edit page.
@require_POST
def updateUser(request):
	user, created = User.objects.update_or_create(
        		pk=request.user.id, defaults={
        				'first_name': request.POST['first_name'],
        				'last_name': request.POST['last_name'],
        				'email': request.POST['email'],
        			}
				)
	messages.error(request, 'User successfully updated', extra_tags='user')
	return redirect('edit')

# Validates billing form and updates billing information. Redirect to edit page.
@require_POST
def updateBilling(request):
	billing_address, created = BillingAddress.objects.update_or_create(
        		user=request.user, defaults={
        				'billingFirstName': request.POST['billing_first_name'],
        				'billingLastName': request.POST['billing_last_name'],
        				'billingAddress': request.POST['billing_address'],
        				'billingCity': request.POST['billing_city'],
        				'billingState': request.POST['billing_state'],
        				'billingPostcode': request.POST['billing_zip_code'],
        				'billingCountry': "US",
        			}
				)
	messages.error(request, 'Billing successfully updated', extra_tags='billing')
	return redirect('edit')

# Validates shippinging form and updates shipping information. Redirect to edit page.
@require_POST
def updateShipping(request):
	shipping_address, created = ShippingAddress.objects.update_or_create(
        		user=request.user, defaults={
        				'shippingFirstName': request.POST['shipping_first_name'],
        				'shippingLastName': request.POST['shipping_last_name'],
        				'shippingAddress': request.POST['shipping_address'],
        				'shippingCity': request.POST['shipping_city'],
        				'shippingState': request.POST['shipping_state'],
        				'shippingPostcode': request.POST['shipping_zip_code'],
        				'shippingCountry': "US",
        			}
        		)
	messages.error(request, 'Shipping successfully updated', extra_tags='shipping')
	return redirect('edit')

