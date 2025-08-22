from rest_framework.routers import DefaultRouter


from django.urls import re_path, include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
    SpectacularJSONAPIView,
)

version = "v0"
router = DefaultRouter()

# router.register("api", api.LandingpageAPIView.as_view(), basename="landingpage")


urlpatterns = [
    # *router.urls,
    path(
        f"{version}/schema/",
        SpectacularJSONAPIView().as_view(),
        name="schema",
    ),
    path(
        f"{version}/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        f"{version}/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
