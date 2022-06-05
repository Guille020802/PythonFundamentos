import unittest
from operaciones import sumar, restar



class TestOperaciones(unittest.TestCase):
    
    def sumar_test(self):
        # creo funcion que evaluará resultados de funcion sumar
        self.assertEqual(sumar(7,8), 15)# compruebo que se cumpla la igualdad
        self.assertEqual(sumar(1,2), 3)
    
    def restar_test(self):
        self.assertEqual(restar(8,7), 1)


if __name__ == '__main__':
    unittest.main()