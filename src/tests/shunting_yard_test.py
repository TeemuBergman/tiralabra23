import unittest
from algorithms.shunting_yard import shunting_yard


class TestShuntingYard(unittest.TestCase):
    """Tests for shunting_yard function in algorithms.shunting_yard module."""

    def test_with_empty_input(self):
        """Test if the function returns None with empty input."""
        rpn = shunting_yard('')
        self.assertEqual(rpn, None)

    def test_with_basic_addition(self):
        """Test if the function converts '1+2' expression to '1 2 +' RPN."""
        rpn = shunting_yard('1+2')
        self.assertEqual(rpn, '1 2 +')

    def test_with_basic_subtraction(self):
        """Test if the function converts '1-2' expression to '1 2 -' RPN."""
        rpn = shunting_yard('1-2')
        self.assertEqual(rpn, '1 2 -')

    def test_with_basic_multiplication(self):
        """Test if the function converts '1*2' expression to '1 2 *' RPN."""
        rpn = shunting_yard('1*2')
        self.assertEqual(rpn, '1 2 *')

    def test_with_basic_division(self):
        """Test if the function converts '1/2' expression to '1 2 /' RPN."""
        rpn = shunting_yard('1/2')
        self.assertEqual(rpn, '1 2 /')

    def test_with_basic_exponentitation(self):
        """Test if the function converts '1^2' expression to '1 2 ^' RPN."""
        rpn = shunting_yard('1^2')
        self.assertEqual(rpn, '1 2 ^')

    def test_with_basic_multiplication_with_negative_values(self):
        """Test if the function converts '-1*(-2)' expression to '1 2 - * -' RPN."""
        rpn = shunting_yard('-1*(-2)')
        self.assertEqual(rpn, '1 2 - * -')

    def test_with_basic_arithmetic_1(self):
        """Test if the function converts '10*(5^2)' expression to '10 5 2 ^ *' RPN."""
        rpn = shunting_yard('10*(5^2)')
        self.assertEqual(rpn, '10 5 2 ^ *')

    def test_with_basic_arithmetic_2(self):
        """Test if the function converts '25*((5^10)/5)' expression to '25 5 10 ^ 5 / *' RPN."""
        rpn = shunting_yard('25*((5^10)/5)')
        self.assertEqual(rpn, '25 5 10 ^ 5 / *')

    def test_with_basic_arithmetic_3(self):
        """Test if the function converts '23+(-27)/(3*3)' expression to '23 27 - 3 3 * / +' RPN."""
        rpn = shunting_yard('23+(-27)/(3*3)')
        self.assertEqual(rpn, '23 27 - 3 3 * / +')

    def test_with_basic_arithmetic_with_errors_1(self):
        """Test if the function converts '(1/2)*(1/2' expression to '1 2 / 1 2 / ( *' RPN."""
        rpn = shunting_yard('(1/2)*(1/2')
        self.assertEqual(rpn, '1 2 / 1 2 / ( *')
