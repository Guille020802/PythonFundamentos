#test_calculator.py

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1, 5), 6)
        
    def test_substract(self):
        self.assertEqual(calculator.subtract(7,8), 1)

if __name__ == '__main__':
    unittest.main()
    
# en consola escribir python -m unittest