# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'), # La ruta vacía (raíz de la app) llamará a home_view
]