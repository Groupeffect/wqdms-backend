from rest_framework import serializers
from interface import models


class MetaSerializer(serializers.ModelSerializer):
    def get_links(self):
        return {}


class VisualizationModelSerializer(MetaSerializer):
    class Meta:
        model = models.Visualization
        fields = "__all__"
