"""Tests for Postfix Evaluator class."""

import unittest

# Custom classes
from algorithms.calculation import Calculation
from algorithms.error_handling import ExpressionError
from algorithms.postfix_evaluator import PostfixEvaluator


class TestPostfixEvaluator(unittest.TestCase):
    """Tests for PostfixEvaluator class."""

    def setUp(self):
        self.calculation = Calculation()
        self.postfix_evaluator = PostfixEvaluator()

    # BASIC TESTS

    def test_basic_addition(self):
        """Test if the function calculates '1 2 +' RPN expression to 3.0."""
        self.calculation.result_rpn = '1 2 +'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.calculation.result, 3)

    def test_basic_subtraction(self):
        """Test if the function calculates '1 2 -' RPN expression to -1.0."""
        self.calculation.result_rpn = '1 2 -'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.calculation.result, -1.0)

    def test_basic_multiplication(self):
        """Test if the function calculates '1 2 *' RPN expression to 2.0."""
        self.calculation.result_rpn = '1 2 *'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.calculation.result, 2)

    def test_basic_division(self):
        """Test if the function calculates '1 2 /' RPN expression to 0.5."""
        self.calculation.result_rpn = '1 2 /'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.calculation.result, 0.5)

    def test_basic_exponentitation(self):
        """Test if the function calculates '1 2 ^' RPN expression to 1.0."""
        self.calculation.result_rpn = '1 2 ^'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.calculation.result, 1)

    def test_negative_values_1(self):
        """Test if the function calculates '-2 2 +' RPN expression to 0.0."""
        self.calculation.result_rpn = '-2 2 +'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.calculation.result, 0)

    def test_negative_values_2(self):
        """Test if the function calculates '-3.5 2 +' RPN expression to -1.5."""
        self.calculation.result_rpn = '-3.5 2 +'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.calculation.result, -1.5)

    def test_basic_arithmetic_1(self):
        """Test if the function calculates '10 5 2 ^ *' RPN expression to 250.0."""
        self.calculation.result_rpn = '10 5 2 ^ *'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.calculation.result, 250)

    def test_basic_arithmetic_2(self):
        """Test if the function calculates '25 5 5 ^ 5 / *' RPN expression to 15625.0."""
        self.calculation.result_rpn = '25 5 5 ^ 5 / *'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.calculation.result, 15625)

    def test_basic_arithmetic_3(self):
        """Test if the function calculates '23 27 + 3 3 * /' RPN expression to 5.555...6."""
        self.calculation.result_rpn = '23 27 + 3 3 * /'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertAlmostEqual(float(self.calculation.result), 5.555555555555555555555555556)

    def test_basic_arithmetic_4(self):
        """Test if the function calculates '6 2 3 ^ *' RPN expression to 48."""
        self.calculation.result_rpn = '6 2 3 ^ *'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.calculation.result, 48)

    def test_negation_1(self):
        """Test if the function calculates '6 2 3 ^ *' RPN expression to 48."""
        self.calculation.result_rpn = '1 -('
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.calculation.result, -1)

    # FUNCTIONS

    def test_function_sine_1(self):
        """Test if the function calculates RPN expression to a correct value."""
        self.calculation.result_rpn = '12 sinr'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertAlmostEqual(float(self.calculation.result), -0.5365729180004349)

    def test_function_sine_2(self):
        """Test if the function calculates RPN expression to a correct value."""
        self.calculation.result_rpn = '-49 sinr'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertAlmostEqual(float(self.calculation.result), 0.9537526527594719)

    def test_function_sine_3(self):
        """Test if the function calculates RPN expression to a correct value."""
        self.calculation.result_rpn = '5 sinr 5 sinr +'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertAlmostEqual(float(self.calculation.result), -1.917848549326276)

    def test_function_cosine_1(self):
        """Test if the function calculates RPN expression to a correct value."""
        self.calculation.result_rpn = '12 cosr'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertAlmostEqual(float(self.calculation.result), 0.8438539587324921)

    def test_function_cosine_2(self):
        """Test if the function calculates RPN expression to a correct value."""
        self.calculation.result_rpn = '-49 cosr'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertAlmostEqual(float(self.calculation.result), 0.3005925437436371)

    def test_function_tangent_1(self):
        """Test if the function calculates RPN expression to a correct value."""
        self.calculation.result_rpn = '12 tanr'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertAlmostEqual(float(self.calculation.result), -0.6358599286615808)

    def test_function_tangent_2(self):
        """Test if the function calculates RPN expression to a correct value."""
        self.calculation.result_rpn = '-49 tanr'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertAlmostEqual(float(self.calculation.result), 3.172908552159191)

    # CONSTANTS

    def test_constant_pi(self):
        """Test if the class returns a correct value of given expression."""
        self.calculation.result_rpn = 'pi'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertAlmostEqual(float(self.calculation.result), 3.1415926535897932)

    def test_constant_tau(self):
        """Test if the class returns a correct value of given expression."""
        self.calculation.result_rpn = 'tau'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertAlmostEqual(float(self.calculation.result), 6.2831853071795864)

    def test_constant_phi(self):
        """Test if the class returns a correct value of given expression."""
        self.calculation.result_rpn = 'phi'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertAlmostEqual(float(self.calculation.result), 1.6180339887498948)

    def test_constant_euler(self):
        """Test if the class returns a correct value of given expression."""
        self.calculation.result_rpn = 'e'
        self.postfix_evaluator.evaluate(self.calculation)
        self.assertAlmostEqual(float(self.calculation.result), 2.7182818284590452)

    # EXCEPTIONS

    def test_empty_input(self):
        """Test with empty input."""
        with self.assertRaises(ExpressionError) as exc:
            self.calculation.result_rpn = ''
            self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual('Error: Expression not found!', str(exc.exception))

    def test_invalid_input_1(self):
        """Test if the function raises OperationError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.calculation.result_rpn = '1 2 / 1 2 / ( *'
            self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual('Error: Not a valid expression!', str(exc.exception))

    def test_invalid_input_2(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.calculation.result_rpn = 'sin'
            self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual('Error: Not a valid expression!', str(exc.exception))

    def test_invalid_decimals_1(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.calculation.result_rpn = '1.1.1.1'
            self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual('Error: Not in decimal format, too many dots!', str(exc.exception))

    def test_invalid_decimals_2(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.calculation.result_rpn = '-2..2'
            self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual('Error: Not in decimal format, too many dots!', str(exc.exception))
