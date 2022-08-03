from django.urls import path

from . import views

app_name = 'dashboard3'

urlpatterns = [
    path('', views.index, name='index'),
]