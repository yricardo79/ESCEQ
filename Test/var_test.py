import unittest
import os
from ESCEQ.Functions import validar_extension
from ESCEQ.variables.invocar_modelo import predecir_puntaje
from registro.views import bus_ser_equ2

class Test_variables(unittest.TestCase):
    def test_bus_ser_equ2(self):
        respuesta = bus_ser_equ2('Magestuoso')
        self.assertTrue(respuesta)   

    def test_valida_ext(self):
        respuesta = validar_extension('jpg')
        self.assertEqual(respuesta,'Incorrecto') 

    def test_bus_ser_equ2fallida(self):
        respuesta = bus_ser_equ2('')
        self.assertFalse(respuesta) 

    def test_predecir_puntaje(self):
        puntaje = predecir_puntaje(0,0,1,0,0,1,0,0.03,0.03,1,0,1,0,1,0,1,2,32,0,1,1,1,0,20)
        self.assertNotEqual(puntaje,50) 
        
    def test_predecir_puntajeFallida(self):
        puntaje = predecir_puntaje(0,0,1,0,0,1,0,0.03,0.03,1,0,1,0,1,0,1,2,50,0,1,1,1,0,90)
        self.assertEqual(puntaje,80) 
 
