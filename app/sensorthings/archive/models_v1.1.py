from django.db import models
from django.contrib.auth import get_user_model
from django_lifecycle import LifecycleModelMixin, hook, BEFORE_SAVE

User = get_user_model()


class SystemAbstractModel(LifecycleModelMixin, models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    uid = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(getattr(self, "name", self.id))

    @hook(BEFORE_SAVE)
    def validate_uid(self):
        exists = (
            self.__class__.objects.exclude(id__in=[self.id])
            .filter(uid=self.uid)
            .values("id")
        )
        if exists:
            self.uid = f"not valid. UID already exists: {list(exists)}"


class ThingWQD(SystemAbstractModel):
    class Meta:
        abstract = True


class Thing(ThingWQD):
    name = models.TextField(db_column="NAME", blank=True, null=True)
    description = models.TextField(db_column="DESCRIPTION", blank=True, null=True)
    properties = models.JSONField(db_column="PROPERTIES", blank=True, null=True)
    id = models.BigAutoField(db_column="ID", primary_key=True)


class ObsPropertyWQD(SystemAbstractModel):
    class Meta:
        abstract = True


class ObsProperty(ObsPropertyWQD):
    name = models.TextField(db_column="NAME", blank=True, null=True)
    definition = models.TextField(db_column="DEFINITION", blank=True, null=True)
    description = models.TextField(db_column="DESCRIPTION", blank=True, null=True)
    properties = models.JSONField(db_column="PROPERTIES", blank=True, null=True)
    id = models.BigAutoField(db_column="ID", primary_key=True)

    class Meta:
        verbose_name_plural = "ObsProperties"


class SensorWQD(SystemAbstractModel):
    class Meta:
        abstract = True


class Sensor(SensorWQD):
    name = models.TextField(db_column="NAME", blank=True, null=True)
    description = models.TextField(db_column="DESCRIPTION", blank=True, null=True)
    properties = models.JSONField(db_column="PROPERTIES", blank=True, null=True)
    encoding_type = models.TextField(db_column="ENCODING_TYPE", blank=True, null=True)
    metadata = models.TextField(db_column="METADATA", blank=True, null=True)
    id = models.BigAutoField(db_column="ID", primary_key=True)


class DatastreamWQD(SystemAbstractModel):
    class Meta:
        abstract = True


class Datastream(DatastreamWQD):
    name = models.TextField(db_column="NAME", blank=True, null=True)
    description = models.TextField(db_column="DESCRIPTION", blank=True, null=True)
    properties = models.JSONField(db_column="PROPERTIES", blank=True, null=True)
    observation_type = models.TextField(
        db_column="OBSERVATION_TYPE", blank=True, null=True
    )
    phenomenon_time_start = models.DateTimeField(
        db_column="PHENOMENON_TIME_START", blank=True, null=True
    )
    phenomenon_time_end = models.DateTimeField(
        db_column="PHENOMENON_TIME_END", blank=True, null=True
    )
    result_time_start = models.DateTimeField(
        db_column="RESULT_TIME_START", blank=True, null=True
    )
    result_time_end = models.DateTimeField(
        db_column="RESULT_TIME_END", blank=True, null=True
    )
    observed_area = models.JSONField(
        db_column="OBSERVED_AREA",
        blank=True,
        null=True,
        help_text="GM_Envelope (GeoJSON Polygon)",
    )  # This field type is GEOJSON.
    sensor = models.ForeignKey(
        "Sensor",
        on_delete=models.DO_NOTHING,
        db_column="SENSOR_ID",
        blank=True,
        null=True,
    )
    obs_property = models.ForeignKey(
        "ObsProperty",
        on_delete=models.DO_NOTHING,
        db_column="OBS_PROPERTY_ID",
        blank=True,
        null=True,
    )
    thing = models.ForeignKey(
        "Thing",
        on_delete=models.DO_NOTHING,
        db_column="THING_ID",
        blank=True,
        null=True,
    )
    unit_name = models.CharField(
        db_column="UNIT_NAME", max_length=255, blank=True, null=True
    )
    unit_symbol = models.CharField(
        db_column="UNIT_SYMBOL", max_length=255, blank=True, null=True
    )
    unit_definition = models.CharField(
        db_column="UNIT_DEFINITION", max_length=255, blank=True, null=True
    )
    last_foi_id = models.BigIntegerField(db_column="LAST_FOI_ID", blank=True, null=True)
    id = models.BigAutoField(db_column="ID", primary_key=True)


class FeatureWQD(SystemAbstractModel):
    class Meta:
        abstract = True


class Feature(FeatureWQD):
    name = models.TextField(db_column="NAME", blank=True, null=True)
    description = models.TextField(db_column="DESCRIPTION", blank=True, null=True)
    properties = models.JSONField(db_column="PROPERTIES", blank=True, null=True)
    encoding_type = models.TextField(db_column="ENCODING_TYPE", blank=True, null=True)
    feature = models.TextField(db_column="FEATURE", blank=True, null=True)
    geom = models.JSONField(
        db_column="GEOM",
        blank=True,
        null=True,
        help_text="GM_Envelope (GeoJSON Polygon)",
    )


class HistoricalLocationWQD(SystemAbstractModel):
    class Meta:
        abstract = True


class HistoricalLocation(HistoricalLocationWQD):
    time = models.DateTimeField(db_column="TIME", blank=True, null=True)
    thing = models.ForeignKey(
        "Thing", on_delete=models.DO_NOTHING, db_column="THING_ID"
    )
    id = models.BigAutoField(db_column="ID", primary_key=True)


class LocationWQD(SystemAbstractModel):
    class Meta:
        abstract = True


class Location(LocationWQD):
    name = models.TextField(db_column="NAME", blank=True, null=True)
    description = models.TextField(db_column="DESCRIPTION", blank=True, null=True)
    properties = models.JSONField(db_column="PROPERTIES", blank=True, null=True)
    encoding_type = models.TextField(db_column="ENCODING_TYPE", blank=True, null=True)
    location = models.TextField(db_column="LOCATION", blank=True, null=True)
    geom = models.JSONField(
        db_column="GEOM",
        blank=True,
        null=True,
        help_text="GM_Envelope (GeoJSON Polygon)",
    )
    gen_foi_id = models.BigIntegerField(db_column="GEN_FOI_ID", blank=True, null=True)
    id = models.BigAutoField(db_column="ID", primary_key=True)


class ObservationWQD(SystemAbstractModel):
    class Meta:
        abstract = True


class Observation(ObservationWQD):
    phenomenon_time_start = models.DateTimeField(
        db_column="PHENOMENON_TIME_START", blank=True, null=True
    )
    phenomenon_time_end = models.DateTimeField(
        db_column="PHENOMENON_TIME_END", blank=True, null=True
    )
    result_time = models.DateTimeField(db_column="RESULT_TIME", blank=True, null=True)
    result_type = models.SmallIntegerField(
        db_column="RESULT_TYPE", blank=True, null=True
    )
    result_number = models.FloatField(db_column="RESULT_NUMBER", blank=True, null=True)
    result_boolean = models.BooleanField(
        db_column="RESULT_BOOLEAN", blank=True, null=True
    )
    result_json = models.JSONField(db_column="RESULT_JSON", blank=True, null=True)
    result_string = models.TextField(db_column="RESULT_STRING", blank=True, null=True)
    result_quality = models.JSONField(db_column="RESULT_QUALITY", blank=True, null=True)
    valid_time_start = models.DateTimeField(
        db_column="VALID_TIME_START", blank=True, null=True
    )
    valid_time_end = models.DateTimeField(
        db_column="VALID_TIME_END", blank=True, null=True
    )
    parameters = models.JSONField(db_column="PARAMETERS", blank=True, null=True)
    datastream = models.ForeignKey(
        "Datastream",
        on_delete=models.DO_NOTHING,
        db_column="DATASTREAM_ID",
        blank=True,
        null=True,
    )
    feature = models.ForeignKey(
        "Feature",
        on_delete=models.DO_NOTHING,
        db_column="FEATURE_ID",
        blank=True,
        null=True,
    )
    id = models.BigAutoField(db_column="ID", primary_key=True)
