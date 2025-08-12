from django.contrib import admin
from waterquality import models

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
