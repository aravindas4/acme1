import csv

from celery import task
from .models import Product


@task
def load_products():
    file_name = '/home/creo/Documents/p.csv'
    file = csv.reader(open(file_name), delimiter=',')
    next(file)

    for line in file:
        obj, created = Product.objects.get_or_create(sku=line[1].upper())
        obj.name = line[0]
        obj.description = line[2]
        obj.save()
