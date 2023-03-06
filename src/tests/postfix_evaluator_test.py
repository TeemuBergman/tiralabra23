"""Tests for Postfix Evaluator class."""

import unittest

# Custom classes
from algorithms.error_handling import ExpressionError, OperationError
from algorithms.postfix_evaluator import PostfixEvaluator


class TestPostfixEvaluator(unittest.TestCase):
    """Tests for PostfixEvaluator class."""

    def setUp(self):
        self.postfix_evaluator = PostfixEvaluator()

    # BASIC TESTS

    def test_basic_addition(self):
        """Test if the function calculates '1 2 +' RPN expression to 3.0."""
        result = self.postfix_evaluator.evaluate('1 2 +')
        self.assertEqual(result, 3.0)

    def test_basic_subtraction(self):
        """Test if the function calculates '1 2 -' RPN expression to -1.0."""
        result = self.postfix_evaluator.evaluate('1 2 -')
        self.assertEqual(result, -1.0)

    def test_basic_multiplication(self):
        """Test if the function calculates '1 2 *' RPN expression to 2.0."""
        result = self.postfix_evaluator.evaluate('1 2 *')
        self.assertEqual(result, 2.0)

    def test_basic_division(self):
        """Test if the function calculates '1 2 /' RPN expression to 0.5."""
        result = self.postfix_evaluator.evaluate('1 2 /')
        self.assertEqual(result, 0.5)

    def test_basic_exponentitation(self):
        """Test if the function calculates '1 2 ^' RPN expression to 1.0."""
        result = self.postfix_evaluator.evaluate('1 2 ^')
        self.assertEqual(result, 1.0)

    def test_negative_values_1(self):
        """Test if the function calculates '-2 2 +' RPN expression to 0.0."""
        result = self.postfix_evaluator.evaluate('-2 2 +')
        self.assertEqual(result, 0.0)

    def test_negative_values_2(self):
        """Test if the function calculates '-3.5 2 +' RPN expression to -1.5."""
        result = self.postfix_evaluator.evaluate('-3.5 2 +')
        self.assertEqual(result, -1.5)

    def test_basic_arithmetic_1(self):
        """Test if the function calculates '10 5 2 ^ *' RPN expression to 250.0."""
        result = self.postfix_evaluator.evaluate('10 5 2 ^ *')
        self.assertEqual(result, 250.0)

    def test_basic_arithmetic_2(self):
        """Test if the function calculates '25 5 5 ^ 5 / *' RPN expression to 15625.0."""
        result = self.postfix_evaluator.evaluate('25 5 5 ^ 5 / *')
        self.assertEqual(result, 15625.0)

    def test_basic_arithmetic_3(self):
        """Test if the function calculates '23 27 + 3 3 * /' RPN expression to 5.555...6."""
        result = self.postfix_evaluator.evaluate('23 27 + 3 3 * /')
        self.assertAlmostEqual(float(result), 5.555555555555555555555555556)

    def test_basic_arithmetic_4(self):
        """Test if the function calculates '6 2 3 ^ *' RPN expression to 48."""
        result = self.postfix_evaluator.evaluate('6 2 3 ^ *')
        self.assertEqual(result, 48.0)

    # FUNCTIONS

    def test_function_sine_1(self):
        """Test if the function calculates RPN expression to a correct value."""
        result = self.postfix_evaluator.evaluate('12 sinr')
        self.assertAlmostEqual(float(result), -0.5365729180004349)

    def test_function_sine_2(self):
        """Test if the function calculates RPN expression to a correct value."""
        result = self.postfix_evaluator.evaluate('-49 sinr')
        self.assertAlmostEqual(float(result), 0.9537526527594719)

    def test_function_sine_3(self):
        """Test if the function calculates RPN expression to a correct value."""
        result = self.postfix_evaluator.evaluate('5 sinr 5 sinr +')
        self.assertAlmostEqual(float(result), -1.917848549326276)

    def test_function_cosine_1(self):
        """Test if the function calculates RPN expression to a correct value."""
        result = self.postfix_evaluator.evaluate('12 cosr')
        self.assertAlmostEqual(float(result), 0.8438539587324921)

    def test_function_cosine_2(self):
        """Test if the function calculates RPN expression to a correct value."""
        result = self.postfix_evaluator.evaluate('-49 cosr')
        self.assertAlmostEqual(float(result), 0.3005925437436371)

    def test_function_tangent_1(self):
        """Test if the function calculates RPN expression to a correct value."""
        result = self.postfix_evaluator.evaluate('12 tanr')
        self.assertAlmostEqual(float(result), -0.6358599286615808)

    def test_function_tangent_2(self):
        """Test if the function calculates RPN expression to a correct value."""
        result = self.postfix_evaluator.evaluate('-49 tanr')
        self.assertAlmostEqual(float(result), 3.172908552159191)

    # EXCEPTIONS

    def test_empty_input(self):
        """Test with empty input."""
        with self.assertRaises(ExpressionError) as exc:
            self.postfix_evaluator.evaluate('')
        self.assertEqual('Error: Expression not found!', str(exc.exception))

    def test_invalid_input_1(self):
        """Test if the function raises OperationError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.postfix_evaluator.evaluate('1 2 / 1 2 / ( *')
        self.assertEqual('Error: Not a complete expression!', str(exc.exception))

    def test_invalid_input_2(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.postfix_evaluator.evaluate('sin')
        self.assertEqual('Error: Not a complete expression!', str(exc.exception))

    def test_invalid_decimals_1(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.postfix_evaluator.evaluate('1.1.1.1')
        self.assertEqual('Error: Not in decimal format, too many dots!', str(exc.exception))

    def test_invalid_decimals_2(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.postfix_evaluator.evaluate('-2..2')
        self.assertEqual('Error: Not in decimal format, too many dots!', str(exc.exception))
