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

    def get(self, request, *args, **kwargs):
        host = getattr(settings, "SERVER_HOST", "http://localhost:8000")
        if self.request.GET.get("format") not in ["api", "json"]:
            return response.Response(
                data={
                    "response": {
                        "data": {
                            "is_vue_app": True,
                            "template": "ui/app/templates/vue.html",
                            "layout": "ui/app/layouts/base.html",
                            "vueApp": "ui/app/vue/app.js",
                            "vueData": "ui/app/data/user.js.vue",
                            "header": "ui/app/headers/header.html",
                            "footer": "ui/app/footers/footer.html",
                            "navbar": "ui/app/navbars/vuenavbar.html",
                            "view": "ui/app/views/Landingpage.html",
                        }
                    }
                }
            )
        return response.Response(data=json.loads(ttags.get_page_urls()))
