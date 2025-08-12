# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class Datastreams(models.Model):
    id = models.BigAutoField(primary_key=True)
    sensor = models.ForeignKey("Sensors", models.DO_NOTHING)
    thing = models.ForeignKey("Things", models.DO_NOTHING)
    ultimate_feature = models.ForeignKey(
        "Features", models.DO_NOTHING, blank=True, null=True
    )
    proximate_feature = models.ForeignKey(
        "Features",
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
    observed_area = models.TextField(
        blank=True, null=True
    )  # This field type is a guess.

    class Meta:
        managed = False
        db_table = "datastreams"


class DatastreamsObservedProperties(models.Model):
    pk = models.CompositePrimaryKey("observed_property_id", "datastream_id")
    observed_property = models.ForeignKey("ObservedProperties", models.DO_NOTHING)
    datastream = models.ForeignKey(Datastreams, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "datastreams_observed_properties"


class FeatureTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "feature_types"


class Features(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    encoding_type = models.TextField(blank=True, null=True)
    feature = models.TextField(blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    properties = models.JSONField(blank=True, null=True)
    creator_sampling = models.ForeignKey(
        "Samplings", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "features"


class HistLocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    thing = models.ForeignKey("Things", models.DO_NOTHING)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "hist_locations"


class Locations(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    encoding_type = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "locations"


class Observations(models.Model):
    id = models.BigAutoField(primary_key=True)
    datastream = models.ForeignKey(Datastreams, models.DO_NOTHING)
    feature = models.ForeignKey(Features, models.DO_NOTHING, blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = "observations"


class ObservedProperties(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "observed_properties"


class PreparationProcedures(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "preparation_procedures"


class PreparationSteps(models.Model):
    id = models.BigAutoField(primary_key=True)
    feature = models.ForeignKey(Features, models.DO_NOTHING)
    preparation_procedure = models.ForeignKey(PreparationProcedures, models.DO_NOTHING)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "preparation_steps"


class RelatedDatastreams(models.Model):
    id = models.BigAutoField(primary_key=True)
    external_target = models.TextField(blank=True, null=True)
    source_datastream = models.ForeignKey(
        Datastreams, models.DO_NOTHING, blank=True, null=True
    )
    target_datastream = models.ForeignKey(
        Datastreams,
        models.DO_NOTHING,
        related_name="relateddatastreams_target_datastream_set",
        blank=True,
        null=True,
    )
    relation_role = models.ForeignKey(
        "RelationRoles", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "related_datastreams"


class RelatedFeatures(models.Model):
    id = models.BigAutoField(primary_key=True)
    external_target = models.TextField(blank=True, null=True)
    source_feature = models.ForeignKey(
        Features, models.DO_NOTHING, blank=True, null=True
    )
    target_feature = models.ForeignKey(
        Features,
        models.DO_NOTHING,
        related_name="relatedfeatures_target_feature_set",
        blank=True,
        null=True,
    )
    relation_role = models.ForeignKey(
        "RelationRoles", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "related_features"


class RelatedObservations(models.Model):
    id = models.BigAutoField(primary_key=True)
    external_target = models.TextField(blank=True, null=True)
    source_observation = models.ForeignKey(
        Observations, models.DO_NOTHING, blank=True, null=True
    )
    target_observation = models.ForeignKey(
        Observations,
        models.DO_NOTHING,
        related_name="relatedobservations_target_observation_set",
        blank=True,
        null=True,
    )
    relation_role = models.ForeignKey(
        "RelationRoles", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "related_observations"


class RelatedThings(models.Model):
    id = models.BigAutoField(primary_key=True)
    external_target = models.TextField(blank=True, null=True)
    source_thing = models.ForeignKey("Things", models.DO_NOTHING, blank=True, null=True)
    target_thing = models.ForeignKey(
        "Things",
        models.DO_NOTHING,
        related_name="relatedthings_target_thing_set",
        blank=True,
        null=True,
    )
    relation_role = models.ForeignKey(
        "RelationRoles", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "related_things"


class RelationRoles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    inverse_name = models.TextField(blank=True, null=True)
    inverse_definition = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "relation_roles"


class SamplerSamplingProcedure(models.Model):
    pk = models.CompositePrimaryKey("sampler_id", "procedure_id")
    sampler = models.ForeignKey("Samplers", models.DO_NOTHING)
    procedure = models.ForeignKey("SamplingProcedures", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "sampler_sampling_procedure"


class Samplers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)
    sampler_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "samplers"


class SamplingProcedures(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sampling_procedures"


class Samplings(models.Model):
    id = models.BigAutoField(primary_key=True)
    thing = models.ForeignKey("Things", models.DO_NOTHING)
    sampled_feature = models.ForeignKey(Features, models.DO_NOTHING)
    sampler = models.ForeignKey(Samplers, models.DO_NOTHING, blank=True, null=True)
    procedure = models.ForeignKey(
        SamplingProcedures, models.DO_NOTHING, blank=True, null=True
    )
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    encoding_type = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    properties = models.JSONField(blank=True, null=True)
    sampling_time_start = models.DateTimeField(blank=True, null=True)
    sampling_time_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "samplings"


class Sensors(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    encoding_type = models.TextField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sensors"


class Things(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    properties = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "things"
