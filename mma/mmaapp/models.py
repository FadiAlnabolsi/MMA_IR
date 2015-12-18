from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Promoter(models.Model):
	user = models.OneToOneField(User, null=True)
	promote = models.BooleanField(default=True)

	def __str__(self):
		return self.user.username

class Event(models.Model):
	promoter = models.OneToOneField(Promoter)
	name = models.TextField()
	poster = models.TextField()

class Fighters(models.Model):
	picture = models.TextField(null=True, blank=True)
	name = models.TextField()
	sherdog_profile = models.TextField()

	def __str__(self):
		return self.name

class Fights(models.Model):
	Event = models.OneToOneField(Event)
	Fighter1 = models.OneToOneField(Fighters)
	Fighter2 = models.OneToOneField(Fighters, related_name="opponent")