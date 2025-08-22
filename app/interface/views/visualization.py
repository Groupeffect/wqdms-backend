from rest_framework import viewsets, response, views
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import (
    TemplateHTMLRenderer,
    BrowsableAPIRenderer,
    JSONRenderer,
)
from django.conf import settings
from interface.serializers import visualization
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict

# from dominate import tags
from django.http import HttpResponse
from datetime import datetime
from interface import models

# import folium
from bs4 import BeautifulSoup
import io
from unittest.mock import patch, mock_open
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView,
)
from django.views.generic.edit import FormView


class StaticHtml(BrowsableAPIRenderer):
    format = "html"
    media_type = "text/html"
    template = "ui/index.html"


class MapHtmlRenderer(BrowsableAPIRenderer):
    format = "html"
    media_type = "text/html"
    template = "ui/app/templates/foliumMap.html"


class Pagination(LimitOffsetPagination):
    default_limit = 1

    def get_paginated_response(self, data):

        if type(data) in [ReturnList] and len(data) > 0:
            return response.Response(data[0])

        return response.Response(data)


class VisualizationModelViewSet(viewsets.ModelViewSet):
    serializer_class = visualization.VisualizationModelSerializer
    http_method_names = ["get", "options"]
    renderer_classes = [StaticHtml, BrowsableAPIRenderer, JSONRenderer]
    pagination_class = Pagination

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()


from django import forms
from django.contrib.gis.forms import (
    OSMWidget,
    OpenLayersWidget,
    GeometryCollectionField,
    GeometryField,
    LineStringField,
    MultiLineStringField,
    MultiPointField,
    MultiPolygonField,
    PointField,
    PolygonField,
)

geom_fields = [
    GeometryCollectionField,
    GeometryField,
    LineStringField,
    MultiLineStringField,
    MultiPointField,
    MultiPolygonField,
    PointField,
    PolygonField,
]

GEOM_FIELDS = {}
for i in geom_fields:

    GEOM_FIELDS[i.__name__] = i


class LocationForm(forms.Form):
    """
    A form to select a single point on a map.
    """

    attrs = {
        "name": "",
        "map_width": 400,
        "map_height": 400,
        "default_lat": 51.5074,  # Default latitude (e.g., London)
        "default_lon": -0.1278,  # Default longitude (e.g., London)
        "default_zoom": 12,
        "display_raw": True,  # Useful for debugging, shows raw coordinates
    }
    PointField = PointField(
        label="Select a Location",
        srid=4326,  # Use WGS84 coordinate system
        widget=OSMWidget(attrs),
    )
    PolygonField = PolygonField(
        label="Select a Poly",
        srid=4326,  # Use WGS84 coordinate system
        widget=OSMWidget(attrs),
    )
