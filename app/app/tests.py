from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    def test_add_number(self):
        res=calc.calculator(5,6)

        self.assertEqual(res,12)

