from django.contrib import admin
from waterquality import models
from django.contrib.admin import AdminSite
from django.contrib.gis.admin import GISModelAdmin


class MapDashboard(AdminSite):
    site_title = "Map"
    site_header = "Map"
    index_title = "Map"


gd = MapDashboard(name="Map")


@admin.register(models.Station, site=gd)
class StationAdmin(GISModelAdmin):
    list_display = ("name", "label", "geometry")
    list_filter = ("tag", "label", "name")
    search_fields = list_filter


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
