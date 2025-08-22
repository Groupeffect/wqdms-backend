from rest_framework import viewsets, permissions, filters
from waterquality.serializers import gis


class StationModelViewSet(viewsets.ModelViewSet):
    serializer_class = gis.StationGeoFeatureModelSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()
