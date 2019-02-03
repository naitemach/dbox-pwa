from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, SignupForm
from .models import *
from django.db import connection
from collections import Counter

def login(request):
	if request.method == 'POST':
		request.session.flush()
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			return render(request,'dbox/signup.html',{})
	else:		
		return render(request,'dbox/index.html',{})
			# user_obj = User.objects.filter(email=form.cleaned_data['email'], password=form.cleaned_data['password'])

			# if user_obj.exists():
			# 	id = user_obj.get().u_id
	# 			order_obj = Order.objects.filter(b_id=id)
	# 			request.session.flush()
	# 			cart = []
	# 			clicked = {}
	# 			request.session['cart'] = cart
	# 			request.session['visited'] = clicked
	# 			request.session['email'] = email
	# 			request.session['first_name'] = user_obj.get().first_name
	# 			request.session['id'] = user_obj.get().u_id
	# 			request.session['credits'] = user_obj.get().wall.credits
	# 			request.session['items'] = len(cart)
	# 			request.session['is_seller'] = user_obj.get().is_seller
	# 			prods=Item.objects.all()
	# 			fprods = []
	# 			inv_id = 1
	# 			inv = request.session.get('visited')
	# 			if (inv) :
	# 				inv_id = max(inv,key=inv.get)
	# 			if request.session.get('cart') is not None:
	# 				items = len(request.session.get('cart'))
	# 			fprods=Item.objects.filter(item_inventory=inv_id)
	# 			if request.session['is_seller'] == 1:
	# 				seller_obj = User.objects.get(u_id=id)
	# 				prods = Item.objects.filter(item_seller=seller_obj)
	# 				return render(request, 'store/sales.html',
	# 							  {'first_name': request.session['first_name'], 'credits': request.session['credits'], 'is_seller': 1,
	# 							   'prods': prods,'id':request.session['id'],'fprods':fprods,'locs':locs})

	# 			else:
	# 				if order_obj.exists():
	# 					return render(request, 'store/index.html', {'first_name': request.session['first_name'],
	# 																'credits': request.session['credits'],
	# 																'items': len(cart),
	# 																'id': request.session['id'],
	# 																'is_seller': request.session['is_seller'],
	# 																'prods': prods,'fprods':fprods,'locs':locs})
	# 				else:
	# 					request.session['items'] = 0
	# 					return render(request, 'store/index.html', {'first_name': request.session['first_name'],
	# 																'credits': request.session['credits'],
	# 																'items': len(cart),
	# 																'id': request.session['id'],
	# 																'is_seller': request.session['is_seller'],
	# 																'prods': prods,'fprods':fprods,'locs':locs})
	# 		error = "Account does not exists. Please register"
	# 		return render(request, 'store/login.html', {'form': form, 'error': error})
	# else:
	# 	form = LoginForm()
	# return render(request, 'store/login.html', {'form': form})

	

def signup(request):
	if request.method == 'POST':
		request.session.flush()
		form = SignupForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			email = form.cleaned_data['email']
			return render(request,'dbox/signup.html',{})
	else:		
		return render(request,'dbox/signup.html',{})

def home(request):
	return render(request,'dbox/home.html',{})

def patient(request):
	return render(request,'dbox/patient.html',{})

def test(request):
	return render(request,'dbox/test.html',{})

