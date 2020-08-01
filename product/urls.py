from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.simple_upload, name='product-upload'),
    path('list/', views.ProductListView.as_view(), name='product-list'),
]