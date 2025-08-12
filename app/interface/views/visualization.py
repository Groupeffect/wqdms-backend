from rest_framework import viewsets, response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import (
    TemplateHTMLRenderer,
    BrowsableAPIRenderer,
    JSONRenderer,
)
from django.conf import settings
from interface.serializers import visualization


class StaticHtml(BrowsableAPIRenderer):
    format = "html"
    media_type = "text/html"
    template = "ui/index.html"


class Pagination(LimitOffsetPagination):
    default_limit = 1

    def get_paginated_response(self, data):
        return response.Response(data[0])


class VisualizationModelViewSet(viewsets.ModelViewSet):
    serializer_class = visualization.VisualizationModelSerializer
    http_method_names = ["get", "options"]
    renderer_classes = [StaticHtml, BrowsableAPIRenderer, JSONRenderer]
    pagination_class = Pagination

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return response.Response(serializer.data)
