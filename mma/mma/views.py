from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/')
	else:
		return render_to_response("invalid.html")

def loggedin(request):
	return render_to_response('loggedin.html',
							 {'full_name': request.user.username })

def invalid_login(request):
	return render_to_response("invalid.html")

def logout(request):
	auth.logout(request)
	return redirect('/')