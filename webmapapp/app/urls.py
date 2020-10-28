from django.urls import path

from .views import *
from . import views


urlpatterns = [
    path('', views.MapPortal.as_view(), name='Homepage')
]

