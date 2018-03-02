from __future__ import absolute_import
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect


from datetime import datetime

from .models import TalkSchedule, Day, Event

def schedule(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    schedule_one = TalkSchedule.objects.filter(conference_day='1').select_related('talk').order_by('start_time')
    schedule_two = TalkSchedule.objects.filter(conference_day='2').select_related('talk').order_by('start_time')

    return render(
        request,
        'schedule.html',
        {
            'title': 'Schedule',
            'message': 'Schedule',
            'year': datetime.now().year,
            'schedule_one': schedule_one,
            'schedule_two': schedule_two,
        }
    )