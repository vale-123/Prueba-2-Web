import unittest
from productos.models import Producto


class testProducto(unittest.TestCase):

    def test_crear_calzado(self):
        producto = Producto.objects.create(numero= 690,
                                       nombre='Zapato Rosa',
                                       precio= 20000,
                                       stock= 100,
                                       tipo='calzado',
                                       activo=1
                                       )
        producto.save()

        self.assertTrue(producto,True)

    def test_crear_acesorios(self):
        producto = Producto.objects.create(numero=363,
                                           nombre='Collar Encaje Lolita',
                                           precio=5000,
                                           stock=67,
                                           tipo='acesorios',
                                           activo=1
                                           )
        producto.save()

        self.assertTrue(producto, True)