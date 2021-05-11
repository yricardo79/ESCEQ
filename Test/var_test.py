import unittest
from ESCEQ.Functions import validar_extension

class Test_variables(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_valida_ext(self):
        respuesta = validar_extension('jpg')
        self.assertEqual(respuesta,'Incorrecto')
