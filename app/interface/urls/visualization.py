from rest_framework import routers
from interface.views import visualization
from django.urls import re_path, path

router = routers.DefaultRouter()
router.register(
    "visualization", visualization.VisualizationModelViewSet, "visualization"
)
urlpatterns = router.urls
