import unittest
from app import celsius_para_fahrenheit, fahrenheit_para_celsius, celsius_para_kelvin

class TestConversor(unittest.TestCase):

    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32.0)
        self.assertEqual(celsius_para_fahrenheit(100), 212.0)
        self.assertEqual(celsius_para_fahrenheit(-40), -40.0)

    def test_fahrenheit_para_celsius(self):
        self.assertEqual(fahrenheit_para_celsius(32), 0.0)
        self.assertEqual(fahrenheit_para_celsius(212), 100.0)
        self.assertEqual(fahrenheit_para_celsius(-40), -40.0)

    def test_celsius_para_kelvin(self):
        self.assertEqual(celsius_para_kelvin(0), 273.15)
        self.assertEqual(celsius_para_kelvin(100), 373.15)

if _name_ == '_main_':
    unittest.main() 
