from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from escola.models import Curso


class CursoTest(APITestCase):
    def setUp(self) -> None:
        self.list_url = reverse("Cursos-list")
        self.curso1 = Curso.objects.create(
            codigo_curso="CTT1",
            descricao="Curso Teste 1",
            nivel="B"
        )
        self.curso2 = Curso.objects.create(
            codigo_curso="CTT2",
            descricao="Curso Teste 2",
            nivel="A"
        )

    # def test_failure(self):
    #     self.fail("Falhou de propósito")

    def test_get_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create(self):
        data = {
            "codigo_curso": "CTT3",
            "descricao": "Curso Teste 3",
            "nivel": "I"
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_course(self):
        response = self.client.delete("/cursos/1/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_course(self):
        data = {
            "codigo_curso": "CTT1",
            "descricao": "Curso Teste 1 Alterado",
            "nivel": "A"
        }
        response = self.client.put("/cursos/1/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
