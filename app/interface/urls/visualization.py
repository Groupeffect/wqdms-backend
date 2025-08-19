from rest_framework import routers
from interface.views import visualization
from django.urls import re_path, path

router = routers.DefaultRouter()
router.register(
    "visualization", visualization.VisualizationModelViewSet, "visualization"
)
urlpatterns = [
    *router.urls,
    path(
        "htmx/<str:tag>/",
        visualization.VisualizationHTMXApiView.as_view(),
        name="htmx",
    ),
    path(
        "htmx/",
        visualization.VisualizationHTMXApiView.as_view(),
        name="htmx",
    ),
    path(
        "map/",
        visualization.VisualizationMapApiView.as_view(),
        name="map",
    ),
    path("geometry/<str:field_type>/", visualization.GeometryListView.as_view()),
]
