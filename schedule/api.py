from rest_framework.viewsets import ModelViewSet

from .serializers import DaySerializer, TalkScheduleSerializer, TalkSerializer, EventSerializer
from .models import Day, TalkSchedule, Event
from talks.models import Proposal


class DayViewSet(ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class TalkScheduleViewSet(ModelViewSet):
    queryset = TalkSchedule.objects.all()
    serializer_class = TalkScheduleSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    