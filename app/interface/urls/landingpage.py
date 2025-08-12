from interface.views import landingpage
from django.urls import re_path

urlpatterns = [
    re_path(
        "",
        landingpage.LandingpageAPIView.as_view(),
        name="landingpage",
    ),
]
