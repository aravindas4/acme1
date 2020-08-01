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


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        load_products(fs.path(filename))
        return redirect('product-list')
    return redirect('product-list')
