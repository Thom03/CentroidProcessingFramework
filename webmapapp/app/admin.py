from django.contrib.gis import admin
from .models import *


# Registering centroid into Admin Page
admin.site.register(parcel_centroid, admin.OSMGeoAdmin)