"""Tests for Postfix Evaluator class."""

import unittest

# Custom classes
from calculator.algorithms.calculation import Calculation
from calculator.algorithms.error_handling import ErrorMessages, ExpressionError
from calculator.algorithms.rpn_evaluator import RPNEvaluator


class TestPostfixEvaluator(unittest.TestCase):
    """Tests for RPNEvaluator class."""

    def setUp(self):
        self.error_message = ErrorMessages()
        self.calculation = Calculation()
        self.postfix_evaluator = RPNEvaluator()

    # BASIC TESTS

    def test_basic_addition(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '1 2 +'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, 3)

    def test_basic_subtraction(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '1 2 -'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, -1.0)

    def test_basic_multiplication(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '1 2 *'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, 2)

    def test_basic_division(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '1 2 /'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, 0.5)

    def test_basic_exponentitation(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '1 2 ^'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, 1)

    def test_negative_values_1(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '0 2 - 2 +'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, 0)

    def test_negative_values_2(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '0 3.5 - 2 +'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, -1.5)

    def test_basic_arithmetic_1(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '10 5 2 ^ *'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, 250)

    def test_basic_arithmetic_2(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '25 5 5 ^ 5 / *'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, 15625)

    def test_basic_arithmetic_3(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '23 27 + 3 3 * /'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertAlmostEqual(float(result), 5.555555555555555555555555556)

    def test_basic_arithmetic_4(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '6 2 3 ^ *'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, 48)

    def test_negation_1(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '0 1 -'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, -1)

    def test_negation_2(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '0 2 2 ^ -'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, -4)

    def test_negation_3(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '0 2 - 0 2 - *'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertEqual(result, 4)

    # FUNCTIONS

    def test_function_sine_1(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '12 sinr'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertAlmostEqual(float(result), -0.5365729180004349)

    def test_function_sine_2(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '0 49 - sinr'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertAlmostEqual(float(result), 0.9537526527594719)

    def test_function_sine_3(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '5 sinr 5 sinr +'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertAlmostEqual(float(result), -1.917848549326276)

    def test_function_cosine_1(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '12 cosr'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertAlmostEqual(float(result), 0.8438539587324921)

    def test_function_cosine_2(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '0 49 - cosr'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertAlmostEqual(float(result), 0.3005925437436371)

    def test_function_tangent_1(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '12 tanr'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertAlmostEqual(float(result), -0.6358599286615808)

    def test_function_tangent_2(self):
        """Test if the function correctly evaluates the given RPN expression."""
        self.calculation.result_rpn = '0 49 - tanr'
        self.postfix_evaluator.evaluate(self.calculation)
        result = self.calculation.result
        self.assertAlmostEqual(float(result), 3.172908552159191)

    # EXCEPTIONS

    def test_empty_input(self):
        """Test with empty input."""
        with self.assertRaises(ExpressionError) as exc:
            self.calculation.result_rpn = ''
            self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.error_message.get('expression not found'),
                         str(exc.exception))

    def test_invalid_input_1(self):
        """Test if the function raises OperationError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.calculation.result_rpn = '1 2 / 1 2 / ( *'
            self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.error_message.get('not a valid expression'),
                         str(exc.exception))

    def test_invalid_input_2(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.calculation.result_rpn = 'sin'
            self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.error_message.get('not a valid expression'),
                         str(exc.exception))

    def test_invalid_decimals_1(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.calculation.result_rpn = '1.1.1.1'
            self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.error_message.get('not a number'),
                         str(exc.exception))

    def test_invalid_decimals_2(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.calculation.result_rpn = '-2..2'
            self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.error_message.get('not a number'),
                         str(exc.exception))

    def test_missing_operator_1(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.calculation.result_rpn = '1 2'
            self.postfix_evaluator.evaluate(self.calculation)
        self.assertEqual(self.error_message.get('not a valid expression'),
                         str(exc.exception))
