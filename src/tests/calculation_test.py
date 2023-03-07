"""Tests for Calculation class."""

import unittest

# Custom classes
from algorithms.error_handling import VariableError
from algorithms.calculation import Calculation


class TestCalculation(unittest.TestCase):
    """Tests for Calculation class."""

    # TESTS INIT

    def setUp(self):
        self.calculation = Calculation()

    # BASIC TESTS

    def test_expression_1(self):
        """Test if the function returns correct expression."""
        self.calculation.new('-1+2-3', '')
        self.assertEqual(self.calculation.expression, '-1+2-3')

    def test_expression_2(self):
        """Test if the function returns correct expression."""
        self.calculation.new('1*2*(-3)', '')
        self.assertEqual(self.calculation.expression, '1*2*(-3)')

    def test_expression_3(self):
        """Test if the function returns correct expression."""
        self.calculation.new('1/2.5*-3', '')
        self.assertEqual(self.calculation.expression, '1/2.5*-3')

    # VARIABLES

    def test_empty_variables(self):
        """Test if the function returns empty string with empty string of variables."""
        self.calculation.new('0', '')
        self.assertEqual(self.calculation.variables, '')

    def test_variables_dictionary_1(self):
        """Test if the function returns correct dictionary with a string of variables."""
        self.calculation.new('0', 'x=1, y=2, z=3')
        self.assertEqual(self.calculation.variables_dictionary, {'x': '1', 'y': '2', 'z': '3'})

    def test_variables_in_expression_1(self):
        """Test if the function returns correct expression with set variables."""
        self.calculation.new('x+y+z', 'x=1,y=2,z=3')
        self.assertEqual(self.calculation.expression, '1+2+3')

    def test_variables_in_expression_2(self):
        """Test if the function returns correct expression with set variables with spaces."""
        self.calculation.new('x+y+z', 'x=1.2, y=2.4, z=3.6')
        self.assertEqual(self.calculation.expression, '1.2+2.4+3.6')

    def est_variables_2(self):
        """Test if the function returns correct dictionary with a string of variables."""
        self.calculation.new('', 'kg=1.5,meter=2,negative=-3')
        self.assertEqual(self.calculation.variables_dictionary, {
            'kg': '1.5', 'meter': '2', 'negative': '-3'
        })

    # FUNCTIONS

    def test_function_sine_1(self):
        """Test if the function returns correct expression."""
        self.calculation.new('sin(12)', '')
        self.assertEqual(self.calculation.expression, 'sin(12)')

    def test_function_sine_2(self):
        """Test if the function returns correct expression."""
        self.calculation.new('sin(12+x)', 'x=1')
        self.assertEqual(self.calculation.expression, 'sin(12+1)')

    def test_function_cosine_1(self):
        """Test if the function returns correct expression."""
        self.calculation.new('cos(12)', '')
        self.assertEqual(self.calculation.expression, 'cos(12)')

    def test_function_tangent_1(self):
        """Test if the function returns correct expression."""
        self.calculation.new('tan(12)', '')
        self.assertEqual(self.calculation.expression, 'tan(12)')

    # EXCEPTIONS

    def test_invalid_variables_1(self):
        """Test if the function returns correct variables."""
        with self.assertRaises(VariableError) as exc:
            self.calculation.new('1+1', 'x=,')
        self.assertEqual('Error: Variable \'x\' has a missing value!', str(exc.exception))

    def test_invalid_variables_2(self):
        """Test if the function returns correct variables."""
        with self.assertRaises(VariableError) as exc:
            self.calculation.new('1+1', 'x=%')
        self.assertEqual('Error: Value \'%\' is not a number!', str(exc.exception))

    def test_invalid_variables_3(self):
        """Test if the function returns correct variables."""
        with self.assertRaises(VariableError) as exc:
            self.calculation.new('1+1', 'x=1,y')
        self.assertEqual('Error: Variable(s) with value missing!', str(exc.exception))
