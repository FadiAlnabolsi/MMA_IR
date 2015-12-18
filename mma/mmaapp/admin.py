from django.contrib import admin
from .models import Promoter, Event, Fighters, Fights
# Register your models here.

admin.site.register(Promoter)
admin.site.register(Event)
admin.site.register(Fighters)
admin.site.register(Fights)