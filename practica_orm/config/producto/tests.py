from django.test import TestCase
from django.urls import reverse
from .models import Fabrica, Producto

class CustomTestCases(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear datos de prueba
        cls.fabrica = Fabrica.objects.create(nombre='Fábrica Prueba', pais='Chile')
        cls.producto = Producto.objects.create(
            nombre='Producto Prueba',
            precio=1500,
            descripcion='Producto de prueba',
            fecha_vencimiento='2025-01-01',
            fabrica=cls.fabrica
        )

    def test_model_content_fabrica(self):
        # Verificar datos del modelo Fábrica
        self.assertEqual(self.fabrica.nombre, 'Fábrica Prueba')
        self.assertEqual(self.fabrica.pais, 'Chile')
        print("Ejecutando test_model_content_fabrica: Verificación de datos de Fábrica. OK")

    def test_model_content_producto(self):
        # Verificar datos del modelo Producto
        self.assertEqual(self.producto.nombre, 'Producto Prueba')
        self.assertEqual(self.producto.descripcion, 'Producto de prueba')
        self.assertEqual(self.producto.precio, 1500)
        print("Ejecutando test_model_content_producto: Verificación de datos de Producto. OK")

    def test_http_response_200_producto(self):
        # Verificar respuesta HTTP 200 para la URL /producto/
        response = self.client.get(reverse('listar_producto'))
        self.assertEqual(response.status_code, 200)
        print("Ejecutando test_http_response_200_producto: Verificación de respuesta HTTP 200 para /producto/. OK")

    def test_mostrar_producto_view(self):
        # Verificar contenido, plantilla y respuesta HTTP 200 para mostrar-producto
        response = self.client.get(reverse('listar_producto'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_productos.html')
        self.assertContains(response, 'Lista productos')
        print("Ejecutando test_mostrar_producto_view: Verificación completa para mostrar-producto. OK")

