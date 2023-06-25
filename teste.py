import unittest
from io import StringIO
from unittest.mock import patch
import IMC

class TestCalculadoraIMC(unittest.TestCase):

    def test_calcImc_abaixo_do_peso(self):
        resultado = IMC.calcImc(50, 1.65)
        self.assertAlmostEqual(resultado, 18.37, places=2)

    def test_calcImc_peso_ideal(self):
        resultado = IMC.calcImc(70, 1.75)
        self.assertAlmostEqual(resultado, 22.86, places=2)

    def test_calcImc_acima_do_peso(self):
        resultado = IMC.calcImc(80, 1.70)
        self.assertAlmostEqual(resultado, 27.68, places=2)

    def test_calcImc_obesidade_grau_I(self):
        resultado = IMC.calcImc(90, 1.80)
        self.assertAlmostEqual(resultado, 27.78, places=2)

    def test_calcImc_obesidade_grau_II(self):
        resultado = IMC.calcImc(100, 1.70)
        self.assertAlmostEqual(resultado, 34.60, places=2)

    def test_calcImc_obesidade_grau_III(self):
        resultado = IMC.calcImc(120, 1.80)
        self.assertAlmostEqual(resultado, 37.04, places=2)

    def test_input_usuario(self):
        with patch('builtins.input', side_effect=['70', '1.75']):
            output = StringIO()
            with patch('sys.stdout', new=output):
                IMC.calcImcUserInput()
                self.assertEqual(output.getvalue().strip(), "Seu IMC é: 22.86\nPeso ideal!")

if __name__ == '__main__':
    unittest.main()
