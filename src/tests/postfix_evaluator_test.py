import unittest
from algorithms.postfix_evaluator import PostfixEvaluator


class TestPostfixEvaluator(unittest.TestCase):
    """Tests for evaluate function in algorithms.evaluate module."""

    def setUp(self):
        self.postfix_evaluator = PostfixEvaluator()

    def test_with_empty_input(self):
        """Test if the function returns None with empty input."""
        result = self.postfix_evaluator.evaluate('')
        self.assertEqual(result, None)

    def test_with_erroneus_input(self):
        """Test if the function returns ValueError with erroneus input."""
        with self.assertRaises(ValueError):
            self.postfix_evaluator.evaluate('1 2 / 1 2 / ( *')

    def test_with_basic_addition(self):
        """Test if the function calculates '1 2 +' RPN expression to 3.0."""
        result = self.postfix_evaluator.evaluate('1 2 +')
        self.assertEqual(result, 3.0)

    def test_with_basic_subtraction(self):
        """Test if the function calculates '1 2 -' RPN expression to -1.0."""
        result = self.postfix_evaluator.evaluate('1 2 -')
        self.assertEqual(result, -1.0)

    def test_with_basic_multiplication(self):
        """Test if the function calculates '1 2 *' RPN expression to 2.0."""
        result = self.postfix_evaluator.evaluate('1 2 *')
        self.assertEqual(result, 2.0)

    def test_with_basic_division(self):
        """Test if the function calculates '1 2 /' RPN expression to 0.5."""
        result = self.postfix_evaluator.evaluate('1 2 /')
        self.assertEqual(result, 0.5)

    def test_with_basic_exponentitation(self):
        """Test if the function calculates '1 2 ^' RPN expression to 1.0."""
        result = self.postfix_evaluator.evaluate('1 2 ^')
        self.assertEqual(result, 1.0)

    def test_with_basic_arithmetic_1(self):
        """Test if the function calculates '10 5 2 ^ *' RPN expression to 250.0."""
        result = self.postfix_evaluator.evaluate('10 5 2 ^ *')
        self.assertEqual(result, 250.0)

    def test_with_basic_arithmetic_2(self):
        """Test if the function calculates '25 5 5 ^ 5 / *' RPN expression to 15625.0."""
        result = self.postfix_evaluator.evaluate('25 5 5 ^ 5 / *')
        self.assertEqual(result, 15625.0)

    def test_with_basic_arithmetic_3(self):
        """Test if the function calculates '23 27 + 3 3 * /' RPN expression to 5.555...6."""
        result = self.postfix_evaluator.evaluate('23 27 + 3 3 * /')
        self.assertEqual(result, 5.555555555555555555555555556)
