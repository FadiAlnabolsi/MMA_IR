from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Event, Fighters, Fights
from mmaapp.forms import EventForm, FighterForm, FightForm

# Create your views here.

def Homepage(request):
		events = Event.objects.all().filter(event_day__gte = timezone.now())
		return render(request, 'homepage.html', {'events':events})

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
	if request.user.is_authenticated():

		if 'submit' in request.POST:
			form = FighterForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/')

			else:
				return render(request, 'addfighter.html', {'form':form})

		form = FighterForm()
		return render(request, 'addfighter.html', {'form':form})

	return redirect('/')

def AddEvent(request):
	if request.user.is_authenticated():

		if 'submit' in request.POST:
			form = EventForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/')

			else:
				return render(request, 'addevent.html', {'form':form})

		form = EventForm()
		return render(request, 'addfighter.html', {'form':form})

	return redirect('/')

def AddFight(request):
	if request.user.is_authenticated():

		if 'submit' in request.POST:
			form = FightForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/')

			else:
				return render(request, 'addfight.html', {'form':form})

		form = FightForm()
		return render(request, 'addfighter.html', {'form':form})

	return redirect('/')

def RemoveEvent(request, event_id):
	if request.user.is_authenticated():
		try:
			Event = Event.objects.get(pk=event_id).delete()
			return redirect('/')
		except Exception as e:
			return redirect('/')

	return redirect('/')

def RemoveFight(request, fight_id):
	if request.user.is_authenticated():
		try:
			Fight = Fights.objects.get(pk=event_id).delete()
			return redirect('/')
		except Exception as e:
			return redirect('/')

	return redirect('/')