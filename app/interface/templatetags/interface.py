from django import template
import json
from django.contrib import admin
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from interface.models import Visualization
from wqdms.settings import SERVER_HOST
from rest_framework.reverse import reverse

from django.template import loader

User = get_user_model()

register = template.Library()

MIMIE_TYPES = ["csv", "rdf", "xml", "json"]


@register.simple_tag
def pre_render_template(path="ui/index.html", context={}):
    t = loader.get_template(path)
    return t.render(context=context)


@register.simple_tag
def raw_template(path="ui/index.html"):
    t = loader.get_template(path)
    return t.template.source


@register.simple_tag
def get_jwt_for_user(user_id):
    user = User.objects.get(id=user_id)
    if not user.is_active:
        raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)
    # return {
    #     "refresh": str(refresh),
    #     "access": str(refresh.access_token),
    # }


@register.simple_tag
def admin_site_title(*args, **kwargs):
    return admin.site.site_title.upper()


@register.simple_tag
def allowed_operation_mimetypes():
    return f"{MIMIE_TYPES}"


@register.simple_tag
def get_host():
    return SERVER_HOST


@register.simple_tag
def get_visualization_list():
    return json.dumps(list(Visualization.objects.all().values()))


@register.simple_tag
def get_service_urls():
    data = [
        {
            "name": "swagger",
        }
    ]
    return json.dumps(data)


@register.simple_tag
def get_page_urls():
    extra = [
        {"name": "admin", "link": get_host() + "/admin/"},
        {"name": "swagger", "link": get_host() + "/api/v0/swagger/"},
        {"name": "redoc", "link": get_host() + "/api/v0/redoc/"},
    ]
    data = [
        {
            "name": i.name,
            "link": get_host() + reverse("visualization-detail", kwargs={"pk": i.pk}),
        }
        for i in list(Visualization.objects.all())
    ] + extra
    return json.dumps(data)


@register.filter
def to_json(item, *args, **kwargs):
    return json.dumps(item)
