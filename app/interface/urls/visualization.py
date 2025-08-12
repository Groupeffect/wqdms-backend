from rest_framework import routers
from interface.views import visualization

router = routers.DefaultRouter()
router.register(
    "visualization", visualization.VisualizationModelViewSet, "visualization"
)
urlpatterns = router.urls
