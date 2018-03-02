from django.contrib import admin

# Register your models here.

from .models import TalkSchedule, Event, Day

admin.site.register(TalkSchedule)
admin.site.register(Event)
admin.site.register(Day)
