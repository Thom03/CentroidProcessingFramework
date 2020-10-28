from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class parcel_centroid(models.Model):
    #  Parcel Centroid Model.
    name = models.CharField(max_length=80)

    # Geometry field(MultiPointField).
    geom = models.MultiPointField(srid=4326)

    # Returns the string representaion of the model.
    def __str__(self):
        return self.name
