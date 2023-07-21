"""Order management app abstractions"""

from django.db import models
from django.db.models.signals import post_delete
from django.utils import timezone

"""Higher level general abstractions"""


class OrderManagementIdentifiable(models.Model):
    """Any model that needs to be identifiable by an ID must implement this class"""

    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True


class CreatedAndUpdatedAware(models.Model):
    """Any class that needs to have created_at and updated_at fields must extend this one"""

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class DeletedAware(models.Model):
    """Any class that needs to have deleted_at fields must extend this one"""

    class Meta:
        abstract = True

    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)

    @property
    def deleted(self):
        return self.deleted_at is not None

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at"])
        post_delete.send(sender=self.__class__, instance=self, using=using)

    def force_delete(self, using=None, *args, **kwargs):
        """Force this object deletion"""
        super(DeletedAware, self).delete(using, *args, **kwargs)

    def restore(self, *args, **kwargs):
        """Restore this instance by setting deleted_at = None
        :param args:
        :param kwargs:
        :return: self.save() result
        """
        self.deleted_at = None
        return self.save(*args, **kwargs)


class SoftDeleteQuerySet(models.QuerySet):
    """A wrapper to just set deleted_at with a value instead of deleting the object itself"""

    def delete(self):
        return self.update(deleted_at=timezone.now())


class SoftDeleteManager(models.Manager):
    """A wrapper to return a SoftDeleteQuerySet to filter 'deleted' objects"""

    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).filter(
            deleted_at__isnull=True
        )

    def get_raw_queryset(self):
        """Return the original QuerySet to list all objects, even those we marked as deleted
        :return: original QuerySet
        """
        return super(SoftDeleteManager, self).get_queryset()


class BaseModel(OrderManagementIdentifiable, CreatedAndUpdatedAware, DeletedAware):
    """Any model must extends our base model to make sure it will have the basic fields we need"""

    class Meta:
        abstract = True

    objects = SoftDeleteManager()
