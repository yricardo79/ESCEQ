import unittest
import os
from ESCEQ.Functions import validar_extension
from ESCEQ.variables.invocar_modelo import predecir_puntaje
from registro.views import bus_ser_equ2
"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown
"""
class Test_variables(unittest.TestCase):   
    def setUp(self):
        self.resultado=1  
        self.puntaje1=1   
        self.puntaje2=1 
        self.puntaje =1
    def test_bus_ser_equ2(self):
        self.resultado = bus_ser_equ2('Magestuoso')
        self.assertTrue(self.resultado) 
    def test_valida_Fallida_ext(self):
        self.resultado = validar_extension('jpg')
        self.assertEqual(self.resultado,'Incorrecto') 
    def test_valida_ext(self):
        self.resultado = validar_extension('.csv')
        self.assertEqual(self.resultado,'Correcto') 
    def test_bus_ser_equ2fallida(self):
        self.resultado = bus_ser_equ2('')
        self.assertFalse(self.resultado) 
    def test_predecir_puntaje(self):
        puntaje = predecir_puntaje(0,0,1,0,0,1,0,0.03,0.03,1,0,1,0,1,0,1,2,32,0,1,1,1,0,20)
        self.assertNotEqual(puntaje,50) 
    def test_predecir_puntajeCalculado(self):
        self.puntaje = predecir_puntaje(0,0,1,0,0,1,0,0.03,0.03,1,0,1,0,1,0,1,2,50,0,1,1,1,0,90)
        self.assertEqual(self.puntaje,68.92) 
    def test_predecir_puntajeDos_Variables(self):
        self.puntaje1 = predecir_puntaje(0,0,1,0,0,1,0,0.03,0.03,1,0,1,0,1,0,1,2,50,0,1,1,1,0,90)
        self.puntaje2 = predecir_puntaje(1,1,1,1,20,50,60,50.12,1.03,1,0,1,0,1,0,1,2,50,0,1,1,1,0,90)
        self.assertLess(self.puntaje1,self.puntaje2)    
    def tearDown(self):
        self.resultado=0
        self.puntaje1 =0
        self.puntaje2=0
        self.puntaje =0