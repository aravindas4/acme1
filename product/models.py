from django.db import models
from model_utils.models import TimeStampedModel

# from .tasks import load_products


class Base(TimeStampedModel):

    class Meta:
        abstract = True


class Product(Base):
    name = models.CharField(max_length=255, null=True)
    sku = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.sku}'
