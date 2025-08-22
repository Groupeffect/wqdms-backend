from django.contrib import admin
from waterquality import models
from django.contrib.admin import AdminSite
from django.contrib.gis.admin import GISModelAdmin


class Management(AdminSite):
    site_title = "Water Quality Management System"
    site_header = "WQDMS"
    index_title = site_title

    # def has_permission(self, request):
    #     return True

    # def has_permission(self, request):
    #     return request.user.groups.filter(name="stations").exists()


management = Management(name="WQDMS")


class MetaAdmin(GISModelAdmin):
    list_display = ("name", "label", "tag", "id")
    list_filter = ("tag", "label", "name", "id")
    search_fields = list_filter


@admin.register(models.Station, site=management)
class StationAdmin(MetaAdmin):
    pass


@admin.register(models.Catchment, site=management)
class CatchmentAdmin(MetaAdmin):
    pass


@admin.register(models.Waterbody, site=management)
class WaterbodyAdmin(MetaAdmin):
    pass


@admin.register(models.Institution, site=management)
class InstitutionAdmin(MetaAdmin):
    pass


admin.site.register(models.Catchment)
admin.site.register(models.Waterbody)
admin.site.register(models.AnalysisMethod)
admin.site.register(models.Fraction)
admin.site.register(models.Institution)
admin.site.register(models.QualityFlag)
admin.site.register(models.Sample)
admin.site.register(models.SampleValue)
admin.site.register(models.Sampling)
admin.site.register(models.Unit)
admin.site.register(models.Measurement)
admin.site.register(models.Station)
