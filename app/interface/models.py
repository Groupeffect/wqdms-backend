import os
from django.db import models
from django.contrib.auth import get_user_model
from django_lifecycle import (
    LifecycleModelMixin,
    hook,
    BEFORE_SAVE,
    AFTER_DELETE,
    BEFORE_DELETE,
)
from django.contrib.contenttypes.models import ContentType
from rdflib import DC, FOAF, SOSA, RDF, RDFS
from django.contrib.gis.db import models as gis_models
from wqdms import meta
from django.conf import settings

# from uuid import uuid4
ONTOLOGIES = ["CUSTOM", "DC", "FOAF", "SOSA", "RDF", "RDFS"]

User = get_user_model()


class SystemAbstractModel(meta.SystemAbstractModel):

    class Meta:
        abstract = True


class ContentTypeAbstractModel(SystemAbstractModel):
    name = models.CharField(max_length=256, blank=True, null=True)
    limit = (
        models.Q(app_label="interface")
        | models.Q(app_label="sensorthings")
        | models.Q(app_label="waterquality")
    )
    entity = models.ForeignKey(
        ContentType,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        help_text="Model name",
        limit_choices_to=limit,
    )
    instance = models.PositiveBigIntegerField(
        blank=True, null=True, help_text="instance id"
    )
    context = models.JSONField(blank=True, null=True, help_text="JSON format")

    class Meta:
        abstract = True


class Description(ContentTypeAbstractModel):
    content = models.TextField(blank=True, null=True, help_text="Description text")


class Geometry(ContentTypeAbstractModel, gis_models.Model):
    limit = (
        models.Q(app_label="sensorthings", model="feature")
        | models.Q(app_label="sensorthings", model="location")
        | models.Q(app_label="waterquality", model="waterbody")
    )
    entity = models.ForeignKey(
        ContentType,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        help_text="Model name",
        limit_choices_to=limit,
    )
    content = models.JSONField(
        blank=True,
        null=True,
        help_text="GeoJSON format",
    )
    point = gis_models.PointField(blank=True, null=True)
    points = gis_models.MultiPointField(blank=True, null=True)
    line = gis_models.LineStringField(blank=True, null=True)
    lines = gis_models.MultiLineStringField(blank=True, null=True)
    polygon = gis_models.PolygonField(blank=True, null=True)
    polygons = gis_models.MultiPolygonField(blank=True, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)
    collection = gis_models.GeometryCollectionField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "geometries"


class Property(ContentTypeAbstractModel):
    limit = models.Q(app_label="sensorthings")
    entity = models.ForeignKey(
        ContentType,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        help_text="Model name",
        limit_choices_to=limit,
    )
    content = models.JSONField(
        blank=True,
        null=True,
        help_text="JSON format",
    )
    key = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "properties"


class Parameter(ContentTypeAbstractModel):
    limit = models.Q(app_label="sensorthings") | models.Q(app_label="waterquality")
    entity = models.ForeignKey(
        ContentType,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        help_text="Model name",
        limit_choices_to=limit,
    )
    content = models.JSONField(
        blank=True,
        null=True,
        help_text="JSON format",
    )
    key = models.TextField(blank=True, null=True)


class PredicateRelation(SystemAbstractModel):
    ontology = models.CharField(choices=[[i, i] for i in ONTOLOGIES])
    name = models.CharField(max_length=256, blank=True, null=True)
    predicate = models.CharField(max_length=256, blank=True, null=True)
    limit = (
        models.Q(app_label="sensorthings")
        | models.Q(app_label="interface")
        | models.Q(app_label="waterquality")
    )
    subject_entity = models.ForeignKey(
        ContentType,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        help_text="Model name",
        limit_choices_to=limit,
        related_name="subject_model",
    )
    subject_instance = models.PositiveBigIntegerField(
        blank=True, null=True, help_text="instance id"
    )
    object_entity = models.ForeignKey(
        ContentType,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        help_text="Model name",
        limit_choices_to=limit,
        related_name="object_model",
    )
    object_instance = models.PositiveBigIntegerField(
        blank=True, null=True, help_text="instance id"
    )

    context = models.JSONField(blank=True, null=True, help_text="JSON format")
    descriptions = models.ManyToManyField(Description, blank=True)

    def __str__(self):
        if self.predicate:
            return f"{self.subject_entity}-{self.object_instance} | {self.predicate} | {self.object_entity}-{self.object_instance}"
        return super().__str__()


def file_upload(instance, filename, *args, **kwargs):
    instance.filename = filename
    # if base64
    # convert and save to instance.base64
    # if mino ...
    # if aws ...
    return f"{instance.owner.id}/{instance.folder}/{filename}"


class FileStorage(LifecycleModelMixin, models.Model):
    encoding = models.CharField(
        max_length=100,
        default="utf-8",
        blank=True,
        null=True,
    )
    delimiter = models.CharField(max_length=3, blank=True, null=True, default=",")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    folder = models.TextField(
        blank=True,
        null=True,
        default="upload",
        help_text="you can set subfolders like : x or x/y/z",
    )
    label = models.CharField(max_length=2000, blank=True, null=True)
    tag = models.CharField(max_length=2000, blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True, default="default")
    link = models.TextField(blank=True, null=True)
    upload = models.FileField(
        verbose_name="Object Upload",
        upload_to=file_upload,
    )
    base64 = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ["owner", "filename", "tag"]

    @hook(BEFORE_DELETE)
    def delete_file_from_minio(self):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.upload.path))


def get_file_choices(folder_name):
    path = os.path.join(
        settings.BASE_DIR, "interface", "templates", "ui", "app", folder_name
    )
    files = os.listdir(path)
    return [
        [
            os.path.join("ui", "app", folder_name, i),
            os.path.join("ui", "app", folder_name, i),
        ]
        for i in files
    ]


class Visualization(SystemAbstractModel):
    class Meta:
        ordering = ["sorting"]

    sorting = models.FloatField(default=0.0)
    domain = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )
    namespace = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )
    label = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )
    tag = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )

    is_vue_app = models.BooleanField(blank=False)
    is_raw = models.BooleanField(blank=False)
    is_raw = models.BooleanField(blank=False)
    is_raw_template = models.BooleanField(blank=False)
    render_string = models.JSONField(
        blank=True,
        null=True,
        help_text='array of keys ["vueApp","template"] will be rendered from string not from template path',
    )
    include = models.JSONField(
        blank=True,
        null=True,
        help_text='array of keys ["vueApp","template"] will be included',
    )
    exclude = models.JSONField(
        blank=True,
        null=True,
        help_text='array of keys ["vueApp","template"] will be excluded',
    )
    context = models.JSONField(blank=True, null=True)
    template = models.CharField(
        choices=get_file_choices("templates"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path of e.g. index.html that will be loaded first",
    )
    layout = models.CharField(
        choices=get_file_choices("layouts"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path of e.g. base.html",
    )
    navbar = models.CharField(
        choices=get_file_choices("navbars"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path or string if 'render_sting' includes key 'navbar'",
    )
    header = models.CharField(
        choices=get_file_choices("headers"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path or string if 'render_sting' includes key 'header'",
    )
    view = models.CharField(
        choices=get_file_choices("views"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path or string if 'render_sting' includes key 'view'",
    )
    footer = models.CharField(
        choices=get_file_choices("footers"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path or string if 'render_sting' includes key 'footer'",
    )
    vueApp = models.CharField(
        choices=get_file_choices("vue"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path or string if 'render_sting' includes key 'vueApp'",
    )
    vueData = models.CharField(
        choices=get_file_choices("data"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path or string if 'render_sting' includes key 'vueData'",
    )
    vueComputed = models.CharField(
        choices=get_file_choices("computed"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path or string if 'render_sting' includes key 'vueComputed'",
    )
    vueMounted = models.CharField(
        choices=get_file_choices("mounted"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path or string if 'render_sting' includes key 'vueMounted'",
    )
    vueCreated = models.CharField(
        choices=get_file_choices("created"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path or string if 'render_sting' includes key 'vueCreated'",
    )
    vueMethods = models.CharField(
        choices=get_file_choices("methods"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path or string if 'render_sting' includes key 'vueMethods'",
    )
    vueTop = models.CharField(
        choices=get_file_choices("top"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path or string if 'render_sting' includes key 'vueTop'",
    )
    vueBottom = models.CharField(
        choices=get_file_choices("bottom"),
        max_length=2000,
        blank=True,
        null=True,
        help_text="template path or string if 'render_sting' includes key 'vueBottom'",
    )
