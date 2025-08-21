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


# class VisualizationHTMXApiView(views.APIView):
#     def get(self, request, tag="button", *args, **kwargs):
#         print(["#### ARGS KWARGS", args, kwargs, tag])
#         tag = getattr(tags, tag)(str(datetime.now()))
#         tag["id"] = "action"
#         tag["hx-target"] = "#main"
#         tag["hx-get"] = "/ui/htmx/code/"
#         tag["hx-sawp"] = "innerHTML"
#         div = tags.div(tag)
#         div["id"] = "#main"
#         html = div.render().replace("\n", "")
#         return HttpResponse(html)


# class VisualizationMapApiView(views.APIView):
#     renderer_classes = [MapHtmlRenderer, BrowsableAPIRenderer, JSONRenderer]

#     def get(self, request, tag=None, *args, **kwargs):
#         DUMMY_FILE_PATH = "memory/my/fake/file.txt"
#         m = folium.Map(location=(0, 0), zoom_start=8)
#         html_template = "ui/app/templates/foliumMap.html"
#         x = models.Geometry.objects.first()
#         geo_json = x.collection.geojson
#         # geojson_data = {}
#         folium.GeoJson(geo_json, name="hello world").add_to(m)

#         folium.LayerControl().add_to(m)

#         with patch("builtins.open", mock_open()) as f:
#             m.save(DUMMY_FILE_PATH)

#             handle = f()
#             # 6. Here is how to GET the string that was written to the mock.
#             #    The 'write' method on the handle is also a mock that records what it was called with.
#             written_content = handle.write.call_args[0][0]
#             _html = written_content.decode("utf-8")
#             html = BeautifulSoup(_html)
#             body = html.find("body")
#             script = html.find_all("script")[-1]
#             styles = html.find_all("style")
#             b = body.__str__()  # .replace("\n", "")
#             s = script.__str__()  # .replace("\n", "")
#             style = "".join([i.__str__() for i in styles])
#             data = {"body": b, "script": s, "styles": style}
#             if self.request.GET.get("slim"):
#                 return HttpResponse(f"{style}{b}{s}")
#             elif self.request.GET.get("script"):
#                 return HttpResponse(
#                     f"{s.replace("<script>","").replace("</script>","")}"
#                 )

#             return response.Response(data=data)


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


class GeometryListView(FormView):
    model = models.Geometry
    template_name = "ui/openlayers/views/widget.html"
    form_class = LocationForm
    map_attrs = {
        "name": "",
        "map_width": 400,
        "map_height": 400,
        "default_lat": 51.5074,  # Default latitude (e.g., London)
        "default_lon": -0.1278,  # Default longitude (e.g., London)
        "default_zoom": 12,
        "display_raw": True,  # Useful for debugging, shows raw coordinates
    }

    def get_form_class(self):
        print("#### class")
        print(self.kwargs)
        ft = self.kwargs.get("field_type")
        field_type = GEOM_FIELDS.get(ft)
        if field_type:
            pass
        return self.form_class

    def get_context_data(self, **kwargs):
        print("CONETX")
        data = super().get_context_data(**kwargs)
        print(data)
        return data
