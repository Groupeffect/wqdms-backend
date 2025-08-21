from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.routers import SimpleRouter, DefaultRouter
from django.db import models as djmodels
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from rest_framework import filters, permissions
from django_filters.rest_framework import DjangoFilterBackend


class MainModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"


class MainModelViewSet(viewsets.ModelViewSet):
    serializer_class = None

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()


class EndpointGenerator:
    def __init__(self, model, fields="__all__", name=None, router=None):
        self.model = model
        self.fields = fields
        self.name = name
        self.router = router
        if router is None:
            self.router = SimpleRouter()

    def get_serializer(self):
        class S(MainModelSerializer):
            class Meta:
                model = self.model
                fields = self.fields

        return type(f"{self.model.__name__}ModelSerializer", (S,), {})

    def get_view(self):
        class V(MainModelViewSet):
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
            serializer_class = self.get_serializer()
            filterset_fields = ["id", "name", "label", "tag", "namespace", "domain"]
            search_fields = filterset_fields
            filter_backends = [
                DjangoFilterBackend,
                filters.SearchFilter,
            ]

        return type(f"{self.model.__name__}ModelViewSet", (V,), {})

    def get_router_url(self):
        if self.name is None:
            self.name = self.model.__name__.lower()
        v = self.get_view()
        self.router.register(self.name, v, basename=self.name)
        return self.router.urls


class ApiEndpoints:
    def __init__(
        self,
        model_modules: list,
        version: str = "v0",
    ):
        self.model_modules = model_modules
        self.urlpatterns = []
        self.version = version

    def get_models(self):
        m = []
        for models in self.model_modules:
            for i in dir(models):
                attr = getattr(models, i)
                if isinstance(attr, djmodels.base.ModelBase) and attr not in [
                    models.SystemAbstractModel,
                    getattr(models, "ContentTypeAbstractModel", None),
                    ContentType,
                    User,
                ]:
                    m.append(attr)
        return m

    def get_endpoints(self):
        for i in self.get_models():
            e = EndpointGenerator(
                model=i,
                name=f"{self.version}/{i.__module__.split(".")[0]}/{i.__name__.lower()}",
            ).get_router_url()
            self.urlpatterns += e

        return self.urlpatterns


from interface import models as interface_models
from waterquality import models as wq_models
from sensorthings import models as sensor_models

y = ApiEndpoints(
    [
        interface_models,
        wq_models,
        sensor_models,
    ]
)
urlpatterns = y.get_endpoints()
