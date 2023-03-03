import unittest

from algorithms.calculation import Calculation
from algorithms.shunting_yard import ShuntingYard


class TestShuntingYard(unittest.TestCase):
    """Tests for shunting_yard function in algorithms.shunting_yard module."""

    def setUp(self):
        self.shunting_yard = ShuntingYard()

    # BASIC TESTS

    def test_empty_input(self):
        """Test if the class returns empty string with empty input."""
        calculation = Calculation('', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '')

    def test_basic_addition(self):
        """Test if the class converts '1+2' expression to '1 2 +'"""
        calculation = Calculation('1+2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 +')

    def test_basic_subtraction(self):
        """Test if the class converts '1-2' expression to '1 2 -'"""
        calculation = Calculation('1-2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 -')

    def test_basic_multiplication(self):
        """Test if the class converts '1*2' expression to '1 2 *'"""
        calculation = Calculation('1*2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 *')

    def test_basic_division(self):
        """Test if the class converts '1/2' expression to '1 2 /'"""
        calculation = Calculation('1/2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 /')

    def test_basic_exponentitation(self):
        """Test if the class converts '1^2' expression to '1 2 ^'"""
        calculation = Calculation('1^2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 ^')

    def test_basic_multiplication_with_negative_values(self):
        """Test if the class converts '-1*(-2)' expression to '1 2 - * -'"""
        calculation = Calculation('-1*(-2)', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '-1 -2 *')

    def test_basic_arithmetic_1(self):
        """Test if the class converts '10*(5^2)' expression to '10 5 2 ^ *'"""
        calculation = Calculation('10.5*(5^2)', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '10.5 5 2 ^ *')

    def test_basic_arithmetic_2(self):
        """Test if the class converts '25*((5^10)/5)' expression to '25 5 10 ^ 5 / *'"""
        calculation = Calculation('25*((5^10)/5)', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '25 5 10 ^ 5 / *')

    def test_basic_arithmetic_3(self):
        """Test if the class converts '23+(-27)/(3*3)' expression to '23 27 - 3 3 * / +'"""
        calculation = Calculation('23+(-27)/(3*3)', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '23 -27 3 3 * / +')

    def test_basic_arithmetic_4(self):
        """Test if the class converts '(-5+2)^2' expression to '-5 2 + 2 ^'"""
        calculation = Calculation('(-5+2)^2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '-5 2 + 2 ^')

    def test_decimals_1(self):
        """Test if the class converts '1.5+2.5' expression to '1.5 2.5 +'"""
        calculation = Calculation('1.5+2.5', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1.5 2.5 +')

    def test_decimals_2(self):
        """Test if the class converts '-8.2/-3.7' expression to '-8.2 -3.7 /'"""
        calculation = Calculation('-8.2/-3.7', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '-8.2 -3.7 /')

    def test_variables_1(self):
        """Test if the class converts 'x+y' expression to '1 2 +'"""
        calculation = Calculation('x+y', 'x=1,y=2')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 +')

    def test_erroneus_expression_1(self):
        """Test if the class converts '(1/2)*(1/2' expression to '1 2 / 1 2 / ( *'"""
        calculation = Calculation('(1/2)*(1/2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 / 1 2 / ( *')

    # FUNCTIONS

    def test_function_sine_1(self):
        """Test if the function calculates '12 SIN' RPN expression to a correct value."""
        calculation = Calculation('sin(12)', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '12 sin')

    # TODO - Lisää testejä!
