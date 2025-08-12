from django.contrib import admin
from interface import models


MODELS = [
    models.Description,
    models.Geometry,
    models.Parameter,
    models.Property,
    models.PredicateRelation,
    models.FileStorage,
    models.Visualization,
]

admin.site.site_header = "WQDMS"
admin.site.site_title = "WQDMS"


def get_app_list(self, request, app_label=None):
    """
    Return a sorted list of all the installed apps that have been
    registered in this site.
    """
    app_dict = self._build_app_dict(request, app_label)

    # Sort the apps alphabetically.
    app_list = sorted(app_dict.values(), key=lambda x: x["name"].lower())

    # # Sort the models alphabetically within each app.
    # for app in app_list:
    #     app["models"].sort(key=lambda x: x["name"])

    return app_list


admin.AdminSite.get_app_list = get_app_list

# Register your models here.
for k, i in enumerate(MODELS):
    admin.site.register(i)
