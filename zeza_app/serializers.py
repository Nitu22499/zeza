from rest_framework import serializers
# from django.core.exceptions import ObjectDoesNotExist

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta :
        model = Event
        fields = '__all__'