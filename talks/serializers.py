from rest_framework import serializers

from .models import Proposal


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        exclude = ('notes', 'status')
