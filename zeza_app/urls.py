from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet

app_name = 'zeza_app'

router = DefaultRouter()
router.register('events', EventViewSet)

urlpatterns = [
    
    path('', include(router.urls))
]
