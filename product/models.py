import csv

from django.db import models
from model_utils.models import TimeStampedModel


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
        file = csv.reader(open('file.csv'), delimiter=',')
        products = []

        count = 0
        for line in file:
            products.append(Product(
                name=line[0],
                sku=line[1],
                description=line[2]))
            count += 1

            if count == 100:
                try:
                    Product.objects.bulk_create(products)
                except Exception as e:
                    print(repr(e))

                products = []
        else:
            try:
                Product.objects.bulk_create(products)
            except Exception as e:
                print(repr(e))


class Product(Base):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.sku}'
