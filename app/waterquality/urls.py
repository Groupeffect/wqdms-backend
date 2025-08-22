from django.urls import path, include
from waterquality import admin
from rest_framework.routers import DefaultRouter
from waterquality.views import api

router = DefaultRouter()
router.register("station", api.StationModelViewSet, "station")

urlpatterns = [
    path("api/", include(router.urls)),
    path("", admin.management.urls),
]
