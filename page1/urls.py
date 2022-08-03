from django.urls import path

from . import views

app_name = 'page1'

urlpatterns = [
    path('tambah/', views.TambahMessage.as_view(), name='tambah'),
    path('edit/<pk>/', views.UpdateMessage.as_view(), name='ubah'),
    path('hapus/<pk>/', views.HapusMessage.as_view(), name='hapus'),
    path('', views.IndexMessage.as_view(), name='index'),
]