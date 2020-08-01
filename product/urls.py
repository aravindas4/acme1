from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_csv, name='product-upload'),
    path('list/', views.ProductListView.as_view(), name='product-list'),
    path('delete/', views.delete_products, name='product-delete'),
]