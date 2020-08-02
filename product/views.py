from django.db.models import Q
from django.views import generic
from .models import Product
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .tasks import load_products


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    queryset = Product.objects.all()
    template_name = 'base.html'
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get('search', None)
        if query:
            object_list = self.queryset.filter(
                Q(name__icontains=query) | Q(sku__icontains=query) | Q(description__icontains=query)
            )
        else:
            object_list = self.queryset.all()

        _filter = self.request.GET.get('is_active', None)

        if _filter == 'True':
            object_list = self.queryset.filter(is_active=True)
        elif _filter == 'False':
            object_list = self.queryset.filter(is_active=False)

        return object_list


def upload_csv(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        load_products.delay(fs.path(filename))
        return redirect('product-list')
    return redirect('product-list')


def delete_products(request):
    if request.method == 'POST':
        Product.objects.all().delete()
        return redirect('product-list')
    return redirect('product-list')
