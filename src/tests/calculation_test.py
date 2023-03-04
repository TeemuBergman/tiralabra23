"""Tests for Calculation class."""

import unittest

# Custom classes
from algorithms.error_handling import VariableError
from algorithms.calculation import Calculation


class TestCalculation(unittest.TestCase):
    """Tests for Calculation class."""

    # BASIC TESTS

    def test_expression_1(self):
        """Test if the function returns correct expression."""
        result = Calculation('-1+2-3', '')
        self.assertEqual(result.expression, '-1+2-3')

    def test_expression_2(self):
        """Test if the function returns correct expression."""
        result = Calculation('1*2*(-3)', '')
        self.assertEqual(result.expression, '1*2*(-3)')

    def test_expression_3(self):
        """Test if the function returns correct expression."""
        result = Calculation('1/2.5*-3', '')
        self.assertEqual(result.expression, '1/2.5*-3')

    # VARIABLES

    def test_empty_variables(self):
        """Test if the function returns empty string with empty string of variables."""
        result = Calculation('', '')
        self.assertEqual(result.variables, '')

    def test_variables_dictionary_1(self):
        """Test if the function returns correct dictionary with a string of variables."""
        result = Calculation('', 'x=1, y=2, z=3')
        self.assertEqual(result.variables_dictionary, {'x': '1', 'y': '2', 'z': '3'})

    def test_variables_in_expression_1(self):
        """Test if the function returns correct expression with set variables."""
        result = Calculation('x+y+z', 'x=1,y=2,z=3')
        self.assertEqual(result.expression, '1+2+3')

    def test_variables_in_expression_2(self):
        """Test if the function returns correct expression with set variables with spaces."""
        result = Calculation('x+y+z', 'x=1.2, y=2.4, z=3.6')
        self.assertEqual(result.expression, '1.2+2.4+3.6')

    def est_variables_2(self):
        """Test if the function returns correct dictionary with a string of variables."""
        result = Calculation('', 'kg=1.5,meter=2,negative=-3')
        self.assertEqual(result, {'kg': '1.5', 'meter': '2', 'negative': '-3'})

    # FUNCTIONS

    def test_function_sine_1(self):
        """Test if the function returns correct expression."""
        result = Calculation('sin(12)', '')
        self.assertEqual(result.expression, 'sin(12)')

    def test_function_sine_2(self):
        """Test if the function returns correct expression."""
        result = Calculation('sin(12+x)', 'x=1')
        self.assertEqual(result.expression, 'sin(12+1)')

    def test_function_cosine_1(self):
        """Test if the function returns correct expression."""
        result = Calculation('cos(12)', '')
        self.assertEqual(result.expression, 'cos(12)')

    def test_function_tangent_1(self):
        """Test if the function returns correct expression."""
        result = Calculation('tan(12)', '')
        self.assertEqual(result.expression, 'tan(12)')

    # EXCEPTIONS

    def test_erroneus_variables_1(self):
        """Test if the function returns correct variables."""
        with self.assertRaises(VariableError) as exc:
            Calculation('1+1', 'x=,')
        self.assertEqual('Error(s) in given variables!', str(exc.exception))

    def test_erroneus_variables_2(self):
        """Test if the function returns correct variables."""
        with self.assertRaises(VariableError) as exc:
            Calculation('1+1', 'x=%')
        self.assertEqual('Variable \'%\' is not a number!', str(exc.exception))
