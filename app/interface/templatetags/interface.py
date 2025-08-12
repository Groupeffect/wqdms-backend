from django.core.management import call_command
from django import template
import json
from django.contrib import admin

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model

User = get_user_model()

register = template.Library()

MIMIE_TYPES = ["csv", "rdf", "xml", "json"]


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


@register.filter
def to_json(item, *args, **kwargs):
    return json.dumps(item)
