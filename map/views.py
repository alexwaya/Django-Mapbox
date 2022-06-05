#from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView

from .models import Place


class AddPlaceView(CreateView):
    model = Place
    template_name = "map/place_form.html"
    success_url = "/index/"
    #fields = ("location", "address")
    fields = ("location", "address", "county_at", "facility_name")


class ChangePlaceView(UpdateView):
    model = Place
    template_name = "map/place_form.html"
    success_url = "/index/"
    #fields = ("location", "address")
    fields = ("location", "address", "county_at", "facility_name")


class PlacesView(ListView):
    model = Place
    template_name = "map/index.html"
    ordering = ["-created_at", ]
