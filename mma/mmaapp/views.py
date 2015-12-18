from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Promoter, Event, Fighters, Fights

# Create your views here.

def Homepage(request):
	if request.user.is_authenticated():
		events = Event.objects.all().filter()
		events = Event.objects.all().filter(event_day__gte = timezone.now())

		return render(request, 'homepage.html', {'events':events})
	else:
		return render(request, 'homepage.html')

def EventPage(request, event_id):
	try:
		event = Event.objects.get(pk=event_id)
		fights = Fights.objects.all().filter(Event=event)
		return render(request, 'eventpage.html', {'event':event, 'fights':fights})
	except Exception as e:
		return redirect('/')

def FighterPage(request, fighter_id):
	try:
		fighter = Fighters.objects.get(pk=fighter_id)
		return render(request, 'fighter.html', {'fighter':fighter})
	except Exception as e:
		return redirect('/')

def AddFighter(request):
	return render(request, 'addfighter.html')

def CreateEvent(request):
	return render(request, 'createevent.html')