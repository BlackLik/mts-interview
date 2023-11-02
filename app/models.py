from django.db import models


class AbstractBaseModel(models.Model):
    one = models.CharField(max_length=100, null=True, blank=True)
    two = models.CharField(max_length=100, null=True, blank=True)
    three = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True


class ModelA(AbstractBaseModel):
    class Meta:
        ordering = ['one', 'two', 'three']


class ModelB(AbstractBaseModel):
    class Meta:
        ordering = ['two', 'three', 'one']


class ModelC(AbstractBaseModel):
    class Meta:
        ordering = ['three', 'one', 'two']
