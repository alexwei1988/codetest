from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import *
from .models import *
from dbopt import Dbcon

# Create your views here.


def login(request):
	if request.method == 'POST':

		form = LoginForm(request.POST)

		if form.is_valid():
			username=form.cleaned_data['uname']
			pwd=form.cleaned_data['pwd']
			mu=Manageruser.objects.all();
			result=mu.filter(uname=username,password=pwd).count()
			if result >=1 :
				request.session['log_in']=True
				request.session.set_expiry(30)
				return  render(request,'navigator.html')
			else :
				request.session['log_in']=False
			
	else:
		form = LoginForm()
	return render(request,'login.html',{'form':form})

def change_password(request):

		if request.session.get('log_in',False):
			
			if request.method == 'POST':

				form = ChangePasswordForm(request.POST)

				if form.is_valid():
					dblist=DbList.objects.all();
					username=form.cleaned_data['uname']
					password=form.cleaned_data['newpwd']
					conn=Dbcon('operation_user','nishi2b',form.data['dbname'])
					conn.changepassword(username,password)
					return HttpResponse('password change successful')

			else:
				form = ChangePasswordForm()				
				return render(request,'change_password.html',{'form':form})

		else:
			form = LoginForm()
			return HttpResponseRedirect(reverse('login'))

def create_user(request):

		if request.session.get('log_in',False):
			
			if request.method == 'POST':

				form = ChangePasswordForm(request.POST)

				if form.is_valid():
					dblist=DbList.objects.all();
					username=form.cleaned_data['uname']
					password=form.cleaned_data['newpwd']
					conn=Dbcon('operation_user','nishi2b',form.data['dbname'])
					conn.changepassword(username,password)
					return HttpResponse('password change successful')

			else:
				form = ChangePasswordForm()				
				return render(request,'change_password.html',{'form':form})

		else:
			form = LoginForm()
			return HttpResponseRedirect(reverse('login'))

