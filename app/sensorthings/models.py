# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth import get_user_model
from django_lifecycle import LifecycleModelMixin, hook, BEFORE_SAVE
from django.contrib.gis.db import models as gis_models
from wqdms import meta

User = get_user_model()


class SystemAbstractModel(meta.SystemAbstractModel):
    owner = None
    domain = models.CharField(max_length=256, blank=True, null=True)
    namespace = models.CharField(max_length=256, blank=True, null=True)
    category = models.CharField(max_length=256, blank=True, null=True)
    label = models.CharField(max_length=256, blank=True, null=True)
    tag = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        abstract = True


class Thing(SystemAbstractModel):

    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)


class Sensor(SystemAbstractModel):

    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    encoding_type = models.TextField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)


class Datastream(SystemAbstractModel, gis_models.Model):

    sensor = models.ForeignKey(
        "Sensor", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    thing = models.ForeignKey(
        "Thing", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    ultimate_feature = models.ForeignKey(
        "Feature", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    proximate_feature = models.ForeignKey(
        "Feature",
        models.DO_NOTHING,
        related_name="datastreams_proximate_feature_set",
        blank=True,
        null=True,
    )
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    result_type = models.JSONField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)
    phenomenon_time_start = models.DateTimeField(blank=True, null=True)
    phenomenon_time_end = models.DateTimeField(blank=True, null=True)
    result_time_start = models.DateTimeField(blank=True, null=True)
    result_time_end = models.DateTimeField(blank=True, null=True)
    observed_area = gis_models.GeometryField(blank=True, null=True)


class FeatureType(SystemAbstractModel):

    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)


class Feature(SystemAbstractModel, gis_models.Model):

    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    encoding_type = models.TextField(blank=True, null=True)
    feature = models.TextField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)
    creator_sampling = models.ForeignKey(
        "Sampling", on_delete=models.DO_NOTHING, blank=True, null=True
    )


class HistLocation(SystemAbstractModel):

    thing = models.ForeignKey(
        "Thing", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    time = models.DateTimeField(blank=True, null=True)


class Location(SystemAbstractModel):

    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    encoding_type = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)

    properties = models.JSONField(blank=True, null=True)


class Observation(SystemAbstractModel):

    datastream = models.ForeignKey(
        Datastream, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    feature = models.ForeignKey(
        Feature, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    phenomenon_time_start = models.DateTimeField(blank=True, null=True)
    phenomenon_time_end = models.DateTimeField(blank=True, null=True)
    result_time = models.DateTimeField(blank=True, null=True)
    valid_time_start = models.DateTimeField(blank=True, null=True)
    valid_time_end = models.DateTimeField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)
    result_type = models.SmallIntegerField(blank=True, null=True)
    result_number = models.FloatField(blank=True, null=True)
    result_boolean = models.BooleanField(blank=True, null=True)
    result_json = models.JSONField(blank=True, null=True)
    result_string = models.TextField(blank=True, null=True)


class ObservedProperty(SystemAbstractModel):

    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "ObservedProperties"


class PreparationProcedure(SystemAbstractModel):

    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)


class PreparationStep(SystemAbstractModel):

    feature = models.ForeignKey(
        Feature, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    preparation_procedure = models.ForeignKey(
        PreparationProcedure,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)


class RelatedDatastream(SystemAbstractModel):

    external_target = models.TextField(blank=True, null=True)
    source_datastream = models.ForeignKey(
        Datastream, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    target_datastream = models.ForeignKey(
        Datastream,
        models.DO_NOTHING,
        related_name="relateddatastreams_target_datastream_set",
        blank=True,
        null=True,
    )
    relation_role = models.ForeignKey(
        "RelationRole", on_delete=models.DO_NOTHING, blank=True, null=True
    )


class RelatedFeature(SystemAbstractModel):

    external_target = models.TextField(blank=True, null=True)
    source_feature = models.ForeignKey(
        Feature, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    target_feature = models.ForeignKey(
        Feature,
        models.DO_NOTHING,
        related_name="relatedfeatures_target_feature_set",
        blank=True,
        null=True,
    )
    relation_role = models.ForeignKey(
        "RelationRole", on_delete=models.DO_NOTHING, blank=True, null=True
    )


class RelatedObservation(SystemAbstractModel):

    external_target = models.TextField(blank=True, null=True)
    source_observation = models.ForeignKey(
        Observation, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    target_observation = models.ForeignKey(
        Observation,
        models.DO_NOTHING,
        related_name="relatedobservations_target_observation_set",
        blank=True,
        null=True,
    )
    relation_role = models.ForeignKey(
        "RelationRole", on_delete=models.DO_NOTHING, blank=True, null=True
    )


class RelatedThing(SystemAbstractModel):

    external_target = models.TextField(blank=True, null=True)
    source_thing = models.ForeignKey(
        "Thing", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    target_thing = models.ForeignKey(
        "Thing",
        models.DO_NOTHING,
        related_name="relatedthings_target_thing_set",
        blank=True,
        null=True,
    )
    relation_role = models.ForeignKey(
        "RelationRole", on_delete=models.DO_NOTHING, blank=True, null=True
    )


class RelationRole(SystemAbstractModel):

    name = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    inverse_name = models.TextField(blank=True, null=True)
    inverse_definition = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)


class Sampler(SystemAbstractModel):

    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)
    sampler_type = models.TextField(blank=True, null=True)


class SamplingProcedure(SystemAbstractModel):

    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)


class Sampling(SystemAbstractModel):

    thing = models.ForeignKey(
        "Thing", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    sampled_feature = models.ForeignKey(
        Feature, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    sampler = models.ForeignKey(
        Sampler, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    procedure = models.ForeignKey(
        SamplingProcedure, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    encoding_type = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)
    sampling_time_start = models.DateTimeField(blank=True, null=True)
    sampling_time_end = models.DateTimeField(blank=True, null=True)
