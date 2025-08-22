from rest_framework_gis.serializers import GeoFeatureModelSerializer
from waterquality import models


class GeoJsonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = None
        geo_field = "geometry"
        fields = "__all__"


class StationGeoFeatureModelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Station
        geo_field = "geometry"
        fields = "__all__"
