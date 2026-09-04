from typing import Any


from django.db import models


class GetOrNoneQuerySet(models.QuerySet):
    """Custom QuerySet that supports get_or_none()"""

    def get_or_none(self, **kwargs):
        try:
            obj = self.get(**kwargs)
            return obj
        except self.model.DoesNotExist:
            return None

class GetOrNoneManager(models.Manager):
    """Adds get_or_none method to objects"""

    def get_queryset(self):
        return GetOrNoneQuerySet(self.model)

    def get_or_none(self, **kwargs):
        return self.get_queryset().get_or_none(**kwargs)
    
class AliveQuerySet(models.QuerySet):
    def alive(self):
        return self.filter(deleted_at__isnull=True)

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class AliveManager(models.Manager):
    def get_queryset(self):
        return AliveQuerySet(self.model, using=self._db).filter(deleted_at__isnull=True)

    def get_or_none(self, **kwargs):
            return self.get_queryset().get_or_none(**kwargs)
    
