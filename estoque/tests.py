from datetime import date, timedelta
from django.test import TestCase
from .models import Insumo

class InsumoTestCase(TestCase):
    def test_alerta_validade_critica(self):
        insumo = Insumo(
            nome="Leite em Pó Integral",
            quantidade=15,
            data_validade=date.today() + timedelta(days=3)
        )
        self.assertEqual(insumo.status_validade(), "CRÍTICO")
