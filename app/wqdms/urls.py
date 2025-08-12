"""
URL configuration for wqdms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import re_path, include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    # re_path("api/auth/", include("rest_framework.urls"), name="auth"),
    # re_path(r"api/", include("api.urls.routes"), name="api"),
    re_path(r"api/", include("api.urls.generator"), name="api"),
    re_path(r"ui/", include("interface.urls.visualization"), name="interface"),
    re_path(r"admin/", admin.site.urls),
    re_path(r"", include("interface.urls.landingpage"), name="start"),
]
