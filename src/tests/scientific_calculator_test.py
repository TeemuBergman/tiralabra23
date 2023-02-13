import unittest
from algorithms.scientific_calculator import ScientificCalculator


class TestScientificCalculator(unittest.TestCase):
    """Tests for ScientificCalculator class in algorithms.scientific_calculator."""

    def setUp(self):
        self.scientific_calculator = ScientificCalculator()

    def test_with_empty_input(self):
        """Test if the class returns None with empty input."""
        expression = ''
        response = self.scientific_calculator.calculate(expression)
        self.assertEqual(response, None)

    def test_with_simple_addition(self):
        """Test if the class returns correct answer with simple input."""
        expression = '1+2'
        response = self.scientific_calculator.calculate(expression)
        self.assertEqual(response, 3.0)

    def test_empty_variables_to_dictionary(self):
        """Test if the method variables_to_dictionary returns correct None with empty variables."""
        variables = ''
        response = self.scientific_calculator.variables_to_dictionary(variables)
        self.assertEqual(response, None)

    def test_variables_to_dictionary_1(self):
        """Test if the method variables_to_dictionary returns correct dictionary."""
        variables = 'x=1,y=2,z=3'
        response = self.scientific_calculator.variables_to_dictionary(variables)
        self.assertEqual(response, {'x': '1', 'y': '2', 'z': '3'})

    def test_variables_to_dictionary_2(self):
        """Test if the method variables_to_dictionary returns correct dictionary."""
        variables = 'kg=1.5,meter=2,negative=-3'
        response = self.scientific_calculator.variables_to_dictionary(variables)
        self.assertEqual(response, {'kg': '1.5', 'meter': '2', 'negative': '-3'})