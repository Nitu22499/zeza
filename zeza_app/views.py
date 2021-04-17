from rest_framework.permissions import AllowAny
from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class EventViewSet(ModelViewSet):
    """
    allowed_methods => GET, POST
    API to store/return Event data
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
