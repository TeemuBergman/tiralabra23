import unittest
from algorithms.calculation import Calculation
from algorithms.shunting_yard import ShuntingYard


class TestShuntingYard(unittest.TestCase):
    """Tests for shunting_yard function in algorithms.shunting_yard module."""

    def setUp(self):
        self.shunting_yard = ShuntingYard()

    def test_with_empty_input(self):
        """Test if the function returns empty string with empty input."""
        calculation = Calculation('', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '')

    def test_with_basic_addition(self):
        """Test if the function converts '1+2' expression to '1 2 +' RPN."""
        calculation = Calculation('1+2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 +')

    def test_with_basic_subtraction(self):
        """Test if the function converts '1-2' expression to '1 2 -' RPN."""
        calculation = Calculation('1-2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 -')

    def test_with_basic_multiplication(self):
        """Test if the function converts '1*2' expression to '1 2 *' RPN."""
        calculation = Calculation('1*2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 *')

    def test_with_basic_division(self):
        """Test if the function converts '1/2' expression to '1 2 /' RPN."""
        calculation = Calculation('1/2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 /')

    def test_with_basic_exponentitation(self):
        """Test if the function converts '1^2' expression to '1 2 ^' RPN."""
        calculation = Calculation('1^2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 ^')

    def test_with_basic_multiplication_with_negative_values(self):
        """Test if the function converts '-1*(-2)' expression to '1 2 - * -' RPN."""
        calculation = Calculation('-1*(-2)', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 - * -')

    def test_with_basic_arithmetic_1(self):
        """Test if the function converts '10*(5^2)' expression to '10 5 2 ^ *' RPN."""
        calculation = Calculation('10*(5^2)', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '10 5 2 ^ *')

    def test_with_basic_arithmetic_2(self):
        """Test if the function converts '25*((5^10)/5)' expression to '25 5 10 ^ 5 / *' RPN."""
        calculation = Calculation('25*((5^10)/5)', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '25 5 10 ^ 5 / *')

    def test_with_basic_arithmetic_3(self):
        """Test if the function converts '23+(-27)/(3*3)' expression to '23 27 - 3 3 * / +' RPN."""
        calculation = Calculation('23+(-27)/(3*3)', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '23 27 - 3 3 * / +')

    def test_with_basic_arithmetic_with_errors_1(self):
        """Test if the function converts '(1/2)*(1/2' expression to '1 2 / 1 2 / ( *' RPN."""
        calculation = Calculation('(1/2)*(1/2', '')
        result = self.shunting_yard.convert(calculation)
        self.assertEqual(result, '1 2 / 1 2 / ( *')
