from django.db import models
from django.contrib.auth import get_user_model
from django_lifecycle import LifecycleModelMixin, hook, BEFORE_SAVE
from django.contrib.contenttypes.models import ContentType
from wqdms import meta

User = get_user_model()


class SystemAbstractModel(meta.SystemAbstractModel):
    name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        abstract = True


class Unit(SystemAbstractModel):
    key = models.CharField(max_length=256, blank=True, null=True)
    label = models.CharField(max_length=256, blank=True, null=True)


class Institution(SystemAbstractModel):
    label = models.CharField(max_length=256, blank=True, null=True)


class QualityFlag(SystemAbstractModel):
    label = models.CharField(max_length=256, blank=True, null=True)


class AnalysisMethod(SystemAbstractModel):
    label = models.CharField(max_length=256, blank=True, null=True)


class Waterbody(SystemAbstractModel):
    label = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name_plural = "waterbodies"


class Sample(SystemAbstractModel):
    label = models.CharField(max_length=256, blank=True, null=True)


class SampleValue(SystemAbstractModel):
    label = models.CharField(max_length=256, blank=True, null=True)


class Sampling(SystemAbstractModel):
    owner = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="user"
    )
    label = models.CharField(max_length=256, blank=True, null=True)


class Fraction(SystemAbstractModel):
    label = models.CharField(max_length=256, blank=True, null=True)


class Catchment(SystemAbstractModel):
    label = models.CharField(max_length=256, blank=True, null=True)
