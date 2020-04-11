from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{}'.format(self.descripcio)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorias"

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)


    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcio, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = "SubCategorias"
        unique_together = ('categoria','descripcion')
