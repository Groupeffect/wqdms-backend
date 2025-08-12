from django.contrib import admin
from sensorthings import models
from django.db import models as djmodels

admin.site.site_header = "WQDMS"
admin.site.site_title = "WQDMS"


def get_models(models=models):
    m = [models.Thing]
    for i in dir(models):
        attr = getattr(models, i)
        if isinstance(attr, djmodels.base.ModelBase) and attr not in [
            models.SystemAbstractModel
        ]:
            m.append(attr)
    return m


def get_app_list(self, request, app_label=None):
    """
    Return a sorted list of all the installed apps that have been
    registered in this site.
    """
    app_dict = self._build_app_dict(request, app_label)

    # Sort the apps alphabetically.
    app_list = sorted(app_dict.values(), key=lambda x: x["name"].lower())

    return app_list


admin.AdminSite.get_app_list = get_app_list

# Register your models here.
for k, i in enumerate(get_models(models)):
    try:
        admin.site.register(i)
    except admin.sites.AlreadyRegistered:
        pass
