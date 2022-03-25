from django.contrib import admin
from django.urls import URLPattern, path
from .views import index, inicio

urlpatterns = [
    path('', index, name='index'),
    path('inicio/', inicio, name='inicio'),
]