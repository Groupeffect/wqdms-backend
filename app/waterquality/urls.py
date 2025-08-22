from django.urls import path, include
from waterquality import admin
from rest_framework.routers import SimpleRouter
from waterquality.views import api

router = SimpleRouter()
router.register("station", api.StationModelViewSet, "station")

urlpatterns = [
    path("api/", include(router.urls)),
    path("", admin.management.urls),
]
