from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['protótipo_banco.json']
    
    def test_carregamento_da_fixtures(self):
        """"Teste que verifica o carregamento da fixtures"""
        estudante = Estudante.objects.get(cpf='28789366980')
        curso = Curso.objects.get(pk=1)
        self.assertEqual (estudante.celular,"60 98611-9878")
        self.assertEqual(curso.codigo,"POO")
