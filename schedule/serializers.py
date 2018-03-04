from rest_framework import serializers

from schedule.models import TalkSchedule, Event, Day
from talks.models import Proposal


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('conference_day')


class TalkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalkSchedule
        fields = all


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        exclude = ('notes', 'abstract', 'status')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = all
