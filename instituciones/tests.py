from django.urls import reverse
from django.test import TestCase, Client

# Create your tests here.

class TestCrearInstitucion(TestCase):
    #Clase para verificar la creaciín de una institución

    def setUp(self):
        #Este método se ejeuta siempre antes de cada caso de prueba
        self.client = Client()
        self.url = reverse("crear")

    def test_crear_institucion(self):
        #Creación de una institución

        datos_entrada = {
            "nombre" : "Nombre",
            "direccion" : "Dirección Válida",
            "fecha_creacion" : "2020-10-10 00:00:00",
            "nif" : "12345678A",
        }

        response = self.client.post(self.url, datos_entrada)
        self.assertContains(response, 'Nombre')
        self.assertContains(response, '12345678A')
        self.assertContains(response, '2020-10-10 00:00:00')
        self.assertContains(response, 'Dirección Válida')