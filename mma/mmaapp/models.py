from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
	name = models.TextField()
	location = models.TextField()
	poster = models.TextField()
	event_day = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Events"

class Fighters(models.Model):
	picture = models.TextField(null=True, blank=True)
	name = models.TextField()
	profile_link = models.TextField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Fighters"

class Fights(models.Model):
	Event = models.ForeignKey(Event, unique=False)
	Fighter1 = models.ForeignKey(Fighters)
	Fighter2 = models.ForeignKey(Fighters, related_name="opponent")
	
	def __str__(self):
		return self.Event.name + ":,  " + self.Fighter1.name + " vs " + self.Fighter2.name

	class Meta:
		verbose_name_plural = "Fights"