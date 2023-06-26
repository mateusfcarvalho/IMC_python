import unittest
from io import StringIO
from unittest.mock import patch
import IMC

class TestCalculadoraIMC(unittest.TestCase):

    def test_calcImc_abaixo_do_peso(self):
        resultado = IMC.calcImc(50, 1.65)
        self.assertEqual(resultado, "Seu IMC é: 18.37\nVocê está abaixo do peso!")

    def test_calcImc_peso_ideal(self):
        resultado = IMC.calcImc(70, 1.75)
        self.assertEqual(resultado, "Seu IMC é: 22.86\nPeso ideal!")

    def test_calcImc_acima_do_peso(self):
        resultado = IMC.calcImc(80, 1.70)
        self.assertEqual(resultado, "Seu IMC é: 27.68\nLevemente acima do peso!")

    def test_calcimc_levemente_acima_do_peso(self):
        resultado = IMC.calcImc(90, 1.80)
        self.assertEqual(resultado, "Seu IMC é: 27.78\nLevemente acima do peso!")

    def test_calcImc_obesidade_grau_I(self):
        resultado = IMC.calcImc(100, 1.70)
        self.assertEqual(resultado, "Seu IMC é: 34.60\nObesidade grau I")

    def test_calcImc_obesidade_grau_II(self):
        resultado = IMC.calcImc(120, 1.80)
        self.assertEqual(resultado, "Seu IMC é: 37.04\nObesidade grau II! (severa)")

    def test_calcImc_obesidade_grau_III(self):
        resultado = IMC.calcImc(200, 1.80)
        self.assertEqual(resultado, "Seu IMC é: 37.04\nObesidade grau III (mórbida)")


 

if __name__ == '__main__':
    unittest.main()
