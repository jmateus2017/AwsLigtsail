from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nombre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('nombre',)
        indexes = [
            models.Index(fields=['nombre']),
        ]
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('tienda:producto_lista_por_categoria', args=[self.slug])

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='productos', default=1,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='productos/%Y/%m/%d', blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True, null=True)
    actualizado = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('tienda:detalle_producto', args=[self.id, self.slug])    
