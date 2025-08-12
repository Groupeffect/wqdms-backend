from django.db import models
from django.contrib.auth import get_user_model
from django_lifecycle import LifecycleModelMixin, hook, BEFORE_SAVE

# from uuid import uuid4

User = get_user_model()

ONTOLOGIES = ["CUSTOM", "DC", "FOAF", "SOSA", "RDF", "RDFS"]


class SystemAbstractModel(LifecycleModelMixin, models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    uid = models.TextField(blank=True, null=True)
    # uuid = models.UUIDField(default=uuid4, auto_created=True) UUID-7

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
