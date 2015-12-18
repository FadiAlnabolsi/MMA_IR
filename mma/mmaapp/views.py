from django.shortcuts import render, redirect
from .models import Promoter, Event, Fighters, Fights

# Create your views here.

def Homepage(request):
	if request.user.is_authenticated():
		return render(request, 'homepage.html')
	else:
		return render(request, 'homepage.html')

def EventPage(request, event_id):
	try:
		event = Event.objects.get(pk=event_id)
	except Exception as e:
		return redirect('/')