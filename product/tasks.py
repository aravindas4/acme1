import csv

from celery import task


@task
def load_products(file, klass):
    file = csv.reader(open(file), delimiter=',')
    products = []

    count = 0
    for line in file:
        products.append(klass(
            name=line[0],
            sku=line[1],
            description=line[2]))
        count += 1

        if count == 100:
            try:
                klass.objects.bulk_create(products)
            except Exception as e:
                print(repr(e))

            products = []
    else:
        try:
            Product.objects.bulk_create(products)
        except Exception as e:
            print(repr(e))

