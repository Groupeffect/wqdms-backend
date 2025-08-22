from rest_framework import views, response
from rest_framework.renderers import (
    TemplateHTMLRenderer,
    BrowsableAPIRenderer,
    JSONRenderer,
)
from django.conf import settings
from interface.templatetags import interface as ttags
import json


class StaticHtml(TemplateHTMLRenderer):
    format = "html"
    media_type = "text/html"
    template_name = "ui/index.html"


class LandingpageAPIView(views.APIView):
    renderer_classes = [StaticHtml, BrowsableAPIRenderer, JSONRenderer]

    def get(self, request, sub=None, pred=None, obj=None, *args, **kwargs):
        host = getattr(settings, "SERVER_HOST", "http://localhost:8000")
        if self.request.GET.get("format") not in ["api", "json"]:
            return response.Response(
                data={
                    "response": {
                        "user": {
                            "is_authenticated": self.request.user.is_authenticated,
                            "is_superuser": self.request.user.is_superuser,
                            "is_staff": self.request.user.is_staff,
                            "name": self.request.user.username,
                        },
                        "host": host,
                        "graph": {"sub": sub, "pred": pred, "obj": obj},
                        "data": {
                            "is_vue_app": True,
                            # "template": "ui/app/templates/vue.html",
                            # "template": "build/index.html",
                            "template": "ui/vueindex.html",
                            "layout": "ui/app/layouts/base.html",
                            "vueApp": "ui/app/vue/app.js",
                            "vueData": "ui/app/data/user.js.vue",
                            "header": "ui/app/headers/header.html",
                            "footer": "ui/app/footers/footer.html",
                            "navbar": "ui/app/navbars/vuenavbar.html",
                            "view": "ui/app/views/Landingpage.html",
                            "script": "build/assets/index.js",
                            "style": "build/assets/index.css",
                        },
                    }
                }
            )
        return response.Response(data=json.loads(ttags.get_page_urls()))
