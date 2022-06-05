from django.db import models
from mapbox_location_field.models import LocationField, AddressAutoHiddenField


class Place(models.Model):
    location = LocationField(
        map_attrs={"style": "mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72", "center": (17.031645, 51.106715)})
    
    created_at = models.DateTimeField(auto_now_add=True)
    address = AddressAutoHiddenField()

    county_at = models.CharField(max_length=255)
    facility_name = models.CharField(max_length=255)

    class Meta:
    	verbose_name = "Facility"
    	verbose_name_plural = "Facilities"

    def __str__(self):
    	return self.facility_name
