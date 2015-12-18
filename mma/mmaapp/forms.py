from django import forms
from mmaapp.models import Event, Fighters, Fights

class EventForm(forms.ModelForm):

	class Meta:
		event_day = forms.DateTimeField(widget=forms.DateTimeInput)
		model = Event
		fields = (
				'name',
				'location',
				'poster',
				'event_day'
				)

class FighterForm(forms.ModelForm):
	picture = forms.CharField(widget=forms.Textarea, label='Image Link')
	profile_link = forms.CharField(widget=forms.Textarea, label='Profile Link (ex. sherdog)')

	class Meta:
		model = Fighters
		fields = (
				'picture',
				'name',
				'profile_link'
				)

class FightForm(forms.ModelForm):

	class Meta:
		model = Fights
		fields = (
				'Event',
				'Fighter1',
				'Fighter2'
				)