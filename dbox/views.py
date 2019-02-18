from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, SignupForm, AddpatForm, SearchpatForm
from .models import *
from django.db import connection
from collections import Counter
from django.utils import timezone

def login(request):
	if request.method == 'POST':
		request.session.flush()
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = Doctor.objects.get(email = email)
			if user.password == password :
				print("Go to home")
				request.session['first_name'] = user.first_name
				request.session['id'] = user.id
				count = Patient.objects.all().count()
				return render(request,'dbox/home.html',{'first_name': request.session['first_name'], 'id' : request.session['id'], 'count' : count , 'mssg':''})	
			else:
				return render(request,'dbox/',{})
	else:		
		return render(request,'dbox/index.html',{})

def signup(request):
	if request.method == 'POST':
		request.session.flush()
		form = SignupForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			obj = Doctor.objects.create() 
			obj.first_name = first_name
			obj.last_name = last_name
			obj.email = email
			obj.password = password
			obj.save()
			request.session['first_name'] = first_name
			request.session['id'] = obj.id
			return render(request,'dbox/home.html',{'first_name': request.session['first_name'], 'id' : request.session['id'], 'count' : count, 'mssg' : '' })	
	else:		
		return render(request,'dbox/signup.html',{})

def home(request):
	count = Patient.objects.all().count()
	return render(request,'dbox/home.html',{'first_name': request.session['first_name'], 'id' : request.session['id'],'count': count,'mssg':''})	

def addpat(request):
	if request.method == 'POST':
		form = AddpatForm(request.POST)
		if form.is_valid():
			obj = Patient.objects.create(age=form.cleaned_data['age']) 
			obj.first_name = form.cleaned_data['first_name']
			obj.last_name = form.cleaned_data['last_name']
			obj.email = form.cleaned_data['email']
			obj.address = form.cleaned_data['address']
			obj.gender = form.cleaned_data['gender']
			obj.age = form.cleaned_data['age']
			obj.contact_no = form.cleaned_data['contact_no']
			obj.doc = Doctor.objects.get(id=request.session.get('id'))
			obj.save()
			mssg="Patient added successfuly"
			count = Patient.objects.all().count()
			return render(request,'dbox/home.html',{'first_name': request.session['first_name'], 'id' : request.session['id'], 'count' : count,'mssg' : mssg })
		else:
			print("dsfsdfsd")
def searchpat(request):
	if request.method == 'POST':
		form = SearchpatForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			mobile = form.cleaned_data['mobile']
			if first_name:
				pat_obj = Patient.objects.get(first_name = first_name) 
			else:
				pat_obj = Patient.objects.get(contact_no = mobile) 
			if pat_obj:
				first_name = pat_obj.first_name
				last_name = pat_obj.last_name
				age = pat_obj.age
				gender = pat_obj.gender
				address = pat_obj.address
				contact_no = pat_obj.contact_no
				#return render(request,'dbox/patient.html',{'first_name':first_name, 'last_name': last_name, 'age': age,'gender': gender,'address': address,'contact_no': contact_no})				
				
				return render(request,'dbox/patient.html',{'pat':pat_obj})				
			else:
				print("Patient not found!")
				return render(request,'dbox/home.html',{})
							
def patient(request):
	return render(request,'dbox/patient.html',{})

def test(request):
	return render(request,'dbox/test.html',{})

