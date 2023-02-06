import unittest
from algorithms.postfix_evaluator import postfix_evaluator


class TestPostfixEvaluator(unittest.TestCase):
    """Tests for postfix_evaluator function in algorithms.postfix_evaluator module."""

    def test_with_empty_input(self):
        """Test if the function returns None with empty input."""
        rpn = postfix_evaluator('')
        self.assertEqual(rpn, None)

    def test_with_erroneus_input(self):
        """Test if the function returns ValueError with erroneus input."""
        with self.assertRaises(ValueError):
            postfix_evaluator('1 2 / 1 2 / ( *')

    def test_with_basic_addition(self):
        """Test if the function calculates '1 2 +' RPN expression to 3.0."""
        rpn = postfix_evaluator('1 2 +')
        self.assertEqual(rpn, 3.0)

    def test_with_basic_subtraction(self):
        """Test if the function calculates '1 2 -' RPN expression to -1.0."""
        rpn = postfix_evaluator('1 2 -')
        self.assertEqual(rpn, -1.0)

    def test_with_basic_multiplication(self):
        """Test if the function calculates '1 2 *' RPN expression to 2.0."""
        rpn = postfix_evaluator('1 2 *')
        self.assertEqual(rpn, 2.0)

    def test_with_basic_division(self):
        """Test if the function calculates '1 2 /' RPN expression to 0.5."""
        rpn = postfix_evaluator('1 2 /')
        self.assertEqual(rpn, 0.5)

    def test_with_basic_exponentitation(self):
        """Test if the function calculates '1 2 ^' RPN expression to 1.0."""
        rpn = postfix_evaluator('1 2 ^')
        self.assertEqual(rpn, 1.0)

    def test_with_basic_arithmetic_1(self):
        """Test if the function calculates '10 5 2 ^ *' RPN expression to 250.0."""
        rpn = postfix_evaluator('10 5 2 ^ *')
        self.assertEqual(rpn, 250.0)

    def test_with_basic_arithmetic_2(self):
        """Test if the function calculates '25 5 5 ^ 5 / *' RPN expression to 15625.0."""
        rpn = postfix_evaluator('25 5 5 ^ 5 / *')
        self.assertEqual(rpn, 15625.0)

    def test_with_basic_arithmetic_3(self):
        """Test if the function calculates '23 27 + 3 3 * /' RPN expression to 5.555...6."""
        rpn = postfix_evaluator('23 27 + 3 3 * /')
        self.assertEqual(rpn, 5.555555555555555555555555556)
