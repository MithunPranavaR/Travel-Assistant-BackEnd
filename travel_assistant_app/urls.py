from django.urls import path
from .views import get_places, save_trip, get_saved_trips

urlpatterns = [
    path('places/', get_places,name="get_places"),
    path('save_trip/', save_trip,name="save_trip"),
    path('get_saved_trips/', get_saved_trips,name="get_saved_trips"),
]