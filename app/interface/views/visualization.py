from rest_framework import viewsets, response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import (
    TemplateHTMLRenderer,
    BrowsableAPIRenderer,
    JSONRenderer,
)
from django.conf import settings
from interface.serializers import visualization
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict


class StaticHtml(BrowsableAPIRenderer):
    format = "html"
    media_type = "text/html"
    template = "ui/index.html"


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
