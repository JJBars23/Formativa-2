from django.test import TestCase
from decimal import Decimal
from .models import Plan


class PlanTests(TestCase):
    def test_precio_formateado_usa_formato_pesos_chilenos(self):
        plan = Plan(precio=Decimal('12990'))

        self.assertEqual(plan.precio_formateado, '$12.990')
