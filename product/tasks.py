import csv
import os

from celery import task
from .models import Product


@task
def load_products(file_1):
    file_name = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_1)
    file = csv.reader(open(file_name), delimiter=',')
    next(file)

    for line in file:
        obj, created = Product.objects.get_or_create(sku=line[1].upper())
        obj.name = line[0]
        obj.description = line[2]
        obj.save()
