"""Tests for Shunting Yard class."""

import unittest

# Custom classes
from algorithms.error_handling import ExpressionError
from algorithms.calculation import Calculation
from algorithms.shunting_yard import ShuntingYard


class TestShuntingYard(unittest.TestCase):
    """Tests for ShuntingYard class."""

    def setUp(self):
        self.calculation = Calculation()
        self.shunting_yard = ShuntingYard()

    # BASIC TESTS

    def test_empty_input(self):
        """Test if the class returns empty string with empty input."""
        self.shunting_yard.convert(self.calculation.new('', ''))
        self.assertEqual(self.calculation.result_rpn, '')

    def test_basic_addition(self):
        """Test if the class converts '1+2' expression to '1 2 +'"""
        self.shunting_yard.convert(self.calculation.new('1+2', ''))
        self.assertEqual(self.calculation.result_rpn, '1 2 +')

    def test_basic_subtraction(self):
        """Test if the class converts '1-2' expression to '1 2 -'"""
        self.shunting_yard.convert(self.calculation.new('1-2', ''))
        self.assertEqual(self.calculation.result_rpn, '1 2 -')

    def test_basic_multiplication(self):
        """Test if the class converts '1*2' expression to '1 2 *'"""
        self.shunting_yard.convert(self.calculation.new('1*2', ''))
        self.assertEqual(self.calculation.result_rpn, '1 2 *')

    def test_basic_division(self):
        """Test if the class converts '1/2' expression to '1 2 /'"""
        self.shunting_yard.convert(self.calculation.new('1/2', ''))
        self.assertEqual(self.calculation.result_rpn, '1 2 /')

    def test_basic_exponentitation(self):
        """Test if the class converts '1^2' expression to '1 2 ^'"""
        self.shunting_yard.convert(self.calculation.new('1^2', ''))
        self.assertEqual(self.calculation.result_rpn, '1 2 ^')

    def test_basic_multiplication_with_negative_values(self):
        """Test if the class converts '-1*(-2)' expression to '1 2 - * -'"""
        self.shunting_yard.convert(self.calculation.new('-1*(-2)', ''))
        self.assertEqual(self.calculation.result_rpn, '-1 -2 *')

    def test_basic_arithmetic_1(self):
        """Test if the class converts '10.5*(5^2)' expression to '10 5 2 ^ *'"""
        self.shunting_yard.convert(self.calculation.new('10.5*(5^2)', ''))
        self.assertEqual(self.calculation.result_rpn, '10.5 5 2 ^ *')

    def test_basic_arithmetic_2(self):
        """Test if the class converts '25*((5^10)/5)' expression to '25 5 10 ^ 5 / *'"""
        self.shunting_yard.convert(self.calculation.new('25*((5^10)/5)', ''))
        self.assertEqual(self.calculation.result_rpn, '25 5 10 ^ 5 / *')

    def test_basic_arithmetic_3(self):
        """Test if the class converts '23+(-27)/(3*3)' expression to '23 27 - 3 3 * / +'"""
        self.shunting_yard.convert(self.calculation.new('23+(-27)/(3*3)', ''))
        self.assertEqual(self.calculation.result_rpn, '23 -27 3 3 * / +')

    def test_basic_arithmetic_4(self):
        """Test if the class converts '(-5+2)^2' expression to '-5 2 + 2 ^'"""
        self.shunting_yard.convert(self.calculation.new('(-5+2)^2', ''))
        self.assertEqual(self.calculation.result_rpn, '-5 2 + 2 ^')

    def test_decimals_1(self):
        """Test if the class converts '1.5+2.5' expression to '1.5 2.5 +'"""
        self.shunting_yard.convert(self.calculation.new('1.5+2.5', ''))
        self.assertEqual(self.calculation.result_rpn, '1.5 2.5 +')

    def test_decimals_2(self):
        """Test if the class converts '-8.2/-3.7' expression to '-8.2 -3.7 /'"""
        self.shunting_yard.convert(self.calculation.new('-8.2/-3.7', ''))
        self.assertEqual(self.calculation.result_rpn, '-8.2 -3.7 /')

    def test_variables_1(self):
        """Test if the class converts 'x+y' expression to '1 2 +'"""
        self.shunting_yard.convert(self.calculation.new('x+y', 'x=1,y=2'))
        self.assertEqual(self.calculation.result_rpn, '1 2 +')

    def test_quite_many_parentheses_1(self):
        """Test if the class converts '((((((((((1+1))))))))))' expression to '1 1 +'"""
        self.shunting_yard.convert(self.calculation.new('((((((((((1+1))))))))))', ''))
        self.assertEqual(self.calculation.result_rpn, '1 1 +')

    def test_quite_many_parentheses_2(self):
        """Test if the class converts '(((((((((((-1)+(1.010101)))))))))))' correctly.'"""
        self.shunting_yard.convert(self.calculation.new('(((((((((((-1)+(1.010101)))))))))))', ''))
        self.assertEqual(self.calculation.result_rpn, '-1 1.010101 +')

    # FUNCTIONS

    def test_function_sine_1(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('sinr(12)', ''))
        self.assertEqual(self.calculation.result_rpn, '12 sinr')

    def test_function_sine_2(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('SINR(12) + 3', ''))
        self.assertEqual(self.calculation.result_rpn, '12 sinr 3 +')

    def test_function_sine_3(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('sinr(3+3)', ''))
        self.assertEqual(self.calculation.result_rpn, '3 3 + sinr')

    def test_function_sine_4(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('sinr(1) + sinr(1)', ''))
        self.assertEqual(self.calculation.result_rpn, '1 sinr 1 sinr +')

    def test_function_sine_5(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('sinr(sinr(1))', ''))
        self.assertEqual(self.calculation.result_rpn, '1 sinr sinr')

    def test_function_cosine_1(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('cosr(12)', ''))
        self.assertEqual(self.calculation.result_rpn, '12 cosr')

    def test_function_cosine_2(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('COSR(12+3)', ''))
        self.assertEqual(self.calculation.result_rpn, '12 3 + cosr')

    def test_function_tangent_1(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('tanr(12)', ''))
        self.assertEqual(self.calculation.result_rpn, '12 tanr')

    def test_function_tangent_2(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('TANR(12+3)', ''))
        self.assertEqual(self.calculation.result_rpn, '12 3 + tanr')

    def test_function_square_root_1(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('sqr(12)', ''))
        self.assertEqual(self.calculation.result_rpn, '12 sqr')

    def test_function_square_root_2(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('SQR(12+3)', ''))
        self.assertEqual(self.calculation.result_rpn, '12 3 + sqr')

    def test_function_logarithm_1(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('log(12)', ''))
        self.assertEqual(self.calculation.result_rpn, '12 log')

    def test_function_logarithm_2(self):
        """Test if the function converts given expression to a correct RPN."""
        self.shunting_yard.convert(self.calculation.new('LOG(12+3)', ''))
        self.assertEqual(self.calculation.result_rpn, '12 3 + log')

    # EXCEPTIONS

    def test_invalid_expression_1(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.shunting_yard.convert(self.calculation.new('(1/2)*(1/2', ''))
        self.assertEqual('Error: Not a valid expression!', str(exc.exception))

    def test_invalid_expression_2(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.shunting_yard.convert(self.calculation.new('sinr12', ''))
        self.assertEqual('Error: Not a valid expression or syntax!', str(exc.exception))
