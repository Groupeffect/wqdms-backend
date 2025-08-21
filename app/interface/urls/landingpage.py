from interface.views import landingpage
from django.urls import re_path, path

urlpatterns = [
    path(
        "",
        landingpage.LandingpageAPIView.as_view(),
        name="landingpage",
    ),
    path(
        "<str:sub>/",
        landingpage.LandingpageAPIView.as_view(),
        name="sub",
    ),
    path(
        "<str:sub>/<str:pred>/",
        landingpage.LandingpageAPIView.as_view(),
        name="subpred",
    ),
    path(
        "<str:sub>/<str:pred>/<str:obj>/",
        landingpage.LandingpageAPIView.as_view(),
        name="subpredobj",
    ),
]
