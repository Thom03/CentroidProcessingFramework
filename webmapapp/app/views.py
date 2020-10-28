from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
from django.core.serializers import serialize
from .models import *



class MapPortal(TemplateView):
    # Rendering portal Template to display Map
    template_name = "portal.html"

def centroid_view(request):
    #Rendering cenroid data to geojson
    centroid_as_geojson = serialize('geojson', parcel_centroid.objects.all())
    return HttpResponse(centroid_as_geojson, content_type='json')
