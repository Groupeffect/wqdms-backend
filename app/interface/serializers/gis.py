from rest_framework_gis.serializers import GeoFeatureModelSerializer
from interface import models


class GeoJsonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = None
        geo_field = "geometry"
        fields = "__all__"
