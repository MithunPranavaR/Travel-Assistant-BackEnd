from django.shortcuts import render
import requests
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from firebase_config import db
#from firebase_admin import db


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def get_places(request):
    destination = request.GET.get("destination","")
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=top+attractions+in+{destination}&key={GOOGLE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)


# Save Trip to Firebase
def save_trip(request):
    data = request.POST
    trip_data = {
        "destination": data.get("destination"),
        "budget": data.get("budget"),
        "interests": data.get("interests"),
        "itinerary": data.get("itinerary"),
    }
    db.collection("saved_trips").add(trip_data)
    return JsonResponse({"message": "Trip saved successfully!"})


# Get Saved Trips from Firebase
def get_saved_trips(request):
    trips = db.collection("saved_trips").stream()
    trip_list = [{trip.id: trip.to_dict()} for trip in trips]
    return JsonResponse({"saved_trips": trip_list})
