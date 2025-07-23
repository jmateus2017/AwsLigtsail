from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Producto

def producto_lista_por_categoria(request, categoria_slug):
    categoria = get_object_or_404(Categoria, slug=categoria_slug)
    productos = Producto.objects.filter(categoria=categoria, disponible=True)
    context = {
        'categoria': categoria,
        'productos': productos,
    }
    return render(request, 'tienda/producto_lista_por_categoria.html', context)

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

def detalle_producto(request, pk, slug):
    producto = get_object_or_404(Producto, pk=pk, slug=slug)
    return render(request, 'tienda/detalle_producto.html', {'producto': producto})

def agregar_al_carrito(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    carrito = request.session.get('carrito', {})
    carrito[str(pk)] = carrito.get(str(pk), 0) + 1
    request.session['carrito'] = carrito
    return redirect('tienda:ver_carrito')


def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0
    for key, cantidad in carrito.items():
        producto = Producto.objects.get(pk=key)
        productos.append({'producto': producto, 'cantidad': cantidad})
        total += producto.precio * cantidad
    context = {'productos': productos, 'total': total}
    return render(request, 'tienda/ver_carrito.html', context)

def eliminar_del_carrito(request, pk):
    carrito = request.session.get('carrito', {})
    carrito.pop(str(pk), None)
    request.session['carrito'] = carrito
    return redirect('tienda:ver_carrito')

def home_view(request):
    ##return HttpResponse("<h1>¡Hola Aplicación XX DjangoLightsail!</h1>")
    return render(request, 'main/home.html')