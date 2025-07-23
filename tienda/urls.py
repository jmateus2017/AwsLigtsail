from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/<int:pk>/<slug:slug>/', views.detalle_producto, name='detalle_producto'),
    path('categoria/<slug:categoria_slug>/', views.producto_lista_por_categoria, name='producto_lista_por_categoria'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:pk>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:pk>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]