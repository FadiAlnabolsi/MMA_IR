from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Promoter(models.Model):
	user = models.OneToOneField(User, null=True)
	promote = models.BooleanField(default=True)

class Event(models.Model):
	promoter = models.OneToOneField(Promoter)
	name = models.TextField()
	poster = models.TextField()

class Fighters(models.Model):
	picture = models.TextField(null=True, blank=True)
	name = models.TextField()
	weight = models.TextField()
	height = models.CharField(max_length=2)
	reach = models.CharField(max_length=2)
	age = models.CharField(max_length=2)

class Fights(models.Model):
	Event = models.OneToOneField(Event)
	Fighter1 = models.OneToOneField(Fighters)
	Fighter2 = models.OneToOneField(Fighters, related_name="opponent")