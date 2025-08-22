from django.db import models
from django_lifecycle import LifecycleModelMixin, hook, BEFORE_SAVE
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db import models as gis_models
from wqdms import meta


class SystemAbstractModel(meta.SystemAbstractModel):

    domain = models.CharField(max_length=256, blank=True, null=True)
    namespace = models.CharField(max_length=256, blank=True, null=True)
    category = models.CharField(max_length=256, blank=True, null=True)
    label = models.CharField(max_length=256, blank=True, null=True)
    tag = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        abstract = True


class Unit(SystemAbstractModel):
    key = models.CharField(max_length=256, blank=True, null=True)


class QualityFlag(SystemAbstractModel):
    pass


class AnalysisMethod(SystemAbstractModel):
    pass


class SampleValue(SystemAbstractModel):
    pass


class Fraction(SystemAbstractModel):
    pass


class Waterbody(SystemAbstractModel, gis_models.Model):
    geometry = gis_models.GeometryCollectionField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "waterbodies"


class Sampling(SystemAbstractModel, gis_models.Model):
    geometry = gis_models.GeometryCollectionField(blank=True, null=True)


class Sample(SystemAbstractModel, gis_models.Model):
    geometry = gis_models.GeometryCollectionField(blank=True, null=True)


class Institution(SystemAbstractModel, gis_models.Model):
    geometry = gis_models.GeometryCollectionField(blank=True, null=True)


class Catchment(SystemAbstractModel, gis_models.Model):
    geometry = gis_models.GeometryCollectionField(blank=True, null=True)


class Station(SystemAbstractModel, gis_models.Model):
    geometry = gis_models.GeometryCollectionField(blank=True, null=True)


class Measurement(SystemAbstractModel, gis_models.Model):
    geometry = gis_models.GeometryCollectionField(blank=True, null=True)
