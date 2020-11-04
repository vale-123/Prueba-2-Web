from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto     = models.AutoField(db_column='id_producto', primary_key=True)
    numero          = models.IntegerField(blank=True, null=True)
    nombre          = models.CharField(max_length=20, blank=True, null=True)
    precio          = models.IntegerField(blank=True, null=True)
    stock           = models.IntegerField(blank=True, null=True)
    foto            = models.ImageField(upload_to='foto', blank=True, null=True)
    tipo            = models.CharField(max_length=20, blank=True, null=True)
    activo          = models.IntegerField(blank=True, null=True)

    def __int__(self):
        return int(self.numero) + ", " + self.precio + ", " + self.stock.__int__()

    def __str__(self):
        return self.nombre + ", " + str(self.tipo) + ", " + self.foto.__str__()

    class Meta:
        ordering = ["numero"]