from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.messages import get_messages

# Create your tests here.

class TestSaveInstitucion(TestCase):
    #Clase para verificar la creaciín de una institución

    def setUp(self):
        #Este método se ejeuta siempre antes de cada caso de prueba
        self.client = Client()
        self.url = reverse("instituciones:crear")

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
        self.assertContains(response, 'Datos almacenados correctamente')


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

    def test_eliminar_institucion(self):    
        datos_entrada = {
                "id" : "",
                "nombre" : "Nombre",
                "direccion" : "Dirección Válida",
                "fecha_creacion" : "2020-10-10 00:00:00",
                "nif" : "12345678A",
            }
        self.client.post(self.url, datos_entrada)

        datos_entrada_eliminar = {
            "id" : "1",
            "confirmado" : "",

        }

        self.url = reverse('instituciones:eliminar')
        response = self.client.get(self.url, datos_entrada_eliminar)
        messages = list(get_messages(response.wsgi_request))
        self.assertRedirects(
            response, 
            '/instituciones/', 
            status_code=302, 
            target_status_code=200, 
            fetch_redirect_response=True
            )
        
        self.assertEqual(str(messages[0]), 'Institucion eliminada')


    