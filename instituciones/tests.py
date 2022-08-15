from django.urls import reverse
from django.test import TestCase, Client

# Create your tests here.

class TestSaveInstitucion(TestCase):
    #Clase para verificar la creaciín de una institución

    def setUp(self):
        #Este método se ejeuta siempre antes de cada caso de prueba
        self.client = Client()
        self.url = reverse("crear")

    def test_save_institucion(self):
        #Creación de una institución correcta

        datos_entrada = {
            "id" : "",
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

    def test_save_institucion_nif_incorrecto(self):
        #Creación de una institución NIF incorrecto

        datos_entrada = {
            "id" : "",
            "nombre" : "Nombre",
            "direccion" : "Dirección Válida",
            "fecha_creacion" : "2020-10-10 00:00:00",
            "nif" : "1234567AA",
        }

        response = self.client.post(self.url, datos_entrada)
        self.assertContains(response, 'No es un formato NIF válido')