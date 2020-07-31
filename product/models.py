from django.db import models
from model_utils.models import TimeStampedModel

from .tasks import load_products


class Base(TimeStampedModel):

    class Meta:
        abstract = True


class FileProductUpload(Base):
    document = models.CharField(max_length=255)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.document}'

    def load_products(self):
        load_products.delay(self.document, Product)


class Product(Base):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.sku}'
