from django.contrib.gis import admin
from .models import *
# Register your models here.

# Registering centroid into Admin Page
admin.site.register(parcel_centroid, admin.OSMGeoAdmin)