"""Tests for Arithmetic Operations class."""

import unittest

# Custom classes
from utils.error_handling import ErrorMessages, OperationError
from calculator.algorithms.arithmetic_operations import ArithmeticOperations


class TestArithmeticOperations(unittest.TestCase):
    """Tests for ArithmeticOperations class."""

    def setUp(self):
        self.error_message = ErrorMessages()
        self.operations = ArithmeticOperations()

    # BASIC TESTS

    def test_basic_addition(self):
        """Test if the function calculates values '1+2' to a result of 3.0."""
        result = self.operations.perform_on('+', 1, 2)
        self.assertEqual(result, 3.0)

    def test_basic_subtraction_1(self):
        """Test if the function calculates values '1-2' to a result of -1.0."""
        result = self.operations.perform_on('-', 1, 2)
        self.assertEqual(result, -1.0)

    def test_basic_subtraction_2(self):
        """Test if the function calculates values '2-1' to a result of 1.0."""
        result = self.operations.perform_on('-', 2, 1)
        self.assertEqual(result, 1.0)

    def test_basic_multiplication(self):
        """Test if the function calculates values '1*2' to a result of 2.0."""
        result = self.operations.perform_on('*', 1, 2)
        self.assertEqual(result, 2.0)

    def test_basic_division_1(self):
        """Test if the function calculates values '1/2' to a result of 0.5."""
        result = self.operations.perform_on('/', 1, 2)
        self.assertEqual(result, 0.5)

    def test_basic_division_2(self):
        """Test if the function calculates values '2/1' to a result of 2.0"""
        result = self.operations.perform_on('/', 2, 1)
        self.assertEqual(result, 2.0)

    def test_basic_exponentitation(self):
        """Test if the function calculates values '1^2' to a result of 1.0."""
        result = self.operations.perform_on('^', 1, 2)
        self.assertEqual(result, 1.0)

    def test_negative_integers(self):
        """Test if the function calculates values '-1-(-2)' to a result of 1.0."""
        result = self.operations.perform_on('-', -1, -2)
        self.assertEqual(result, 1.0)

    def test_negative_float(self):
        """Test if the function calculates values '1^2' to a result of 1.0."""
        result = self.operations.perform_on('-', -1.6, -2.2)
        self.assertAlmostEqual(float(result), 0.6)

    # FUNCTIONS

    def test_function_sine_radians(self):
        """Test if the function evaluates given expression correctly."""
        result = self.operations.perform_on('sinr', 12)
        self.assertAlmostEqual(float(result), -0.5365729180004349)

    def test_function_sine_degrees(self):
        """Test if the function evaluates given expression correctly."""
        result = self.operations.perform_on('sind', 12)
        self.assertAlmostEqual(float(result), 0.20791169081775934)

    def test_function_cosine_radians(self):
        """Test if the function evaluates given expression correctly."""
        result = self.operations.perform_on('cosr', 12)
        self.assertAlmostEqual(float(result), 0.8438539587324921)

    def test_function_cosine_degrees(self):
        """Test if the function evaluates given expression correctly."""
        result = self.operations.perform_on('cosd', 12)
        self.assertAlmostEqual(float(result), 0.9781476007338057)

    def test_function_tangent_radians(self):
        """Test if the function evaluates given expression correctly."""
        result = self.operations.perform_on('tanr', 12)
        self.assertAlmostEqual(float(result), -0.6358599286615808)

    def test_function_tangent_degrees(self):
        """Test if the function evaluates given expression correctly."""
        result = self.operations.perform_on('tand', 12)
        self.assertAlmostEqual(float(result), 0.21255656167002213)

    def test_function_square_root(self):
        """Test if the function evaluates given expression correctly."""
        result = self.operations.perform_on('sqrt', 12)
        self.assertAlmostEqual(float(result), 3.4641016151377544)

    def test_function_logarithm(self):
        """Test if the function evaluates given expression correctly."""
        result = self.operations.perform_on('log', 12)
        self.assertAlmostEqual(float(result), 2.4849066497880004)

    def test_function_random(self):
        """Test if the function evaluates given expression correctly."""
        result = self.operations.perform_on('rand', 200)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 200)

    # EXCEPTIONS

    def test_division_by_zero(self):
        """Test if the function can divide with zero"""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('/', 1, 0)
        self.assertEqual(self.error_message.get('division by zero'),
                         str(exc.exception))

    def test_no_operand(self):
        """Test if the function works with no operator at all."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('', 0)
        self.assertEqual(self.error_message.get('missing operand'),
                         str(exc.exception))

    def test_invalid_operator_1(self):
        """Test if the function resolves invalid operator to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('%', 1, 0)
        self.assertEqual(self.error_message.get('missing operand'),
                         str(exc.exception))

    def test_invalid_operator_2(self):
        """Test if the function resolves invalid operator to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('s', 4, 4)
        self.assertEqual(self.error_message.get('missing operand'),
                         str(exc.exception))

    def test_function_square_root_negative(self):
        """Test if the function resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('sqrt', -4)
        self.assertEqual(self.error_message.get('square root'),
                         str(exc.exception))

    def test_function_logarithm_negative(self):
        """Test if the function resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('log', -4)
        self.assertEqual(self.error_message.get('logarithm'),
                         str(exc.exception))

    def test_function_sine_radians_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('sinr')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_sine_degrees_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('sind')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_cosine_radians_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('cosr')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_cosine_degrees_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('cosd')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_tangent_radians_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('tanr')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_tangent_degrees_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('tand')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_logarithm_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('log')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_square_root_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('sqrt')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_negation_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('-(')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_operation_addition_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('+')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_operation_subtraction_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('-')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_operation_multiplication_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('*')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_operation_division_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('/')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_operation_exponentitation_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('^')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_random_no_value(self):
        """Test if the function handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('rand')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_random_negative(self):
        """Test if the function resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('rand', -4)
        self.assertEqual(self.error_message.get('random'),
                         str(exc.exception))

    def test_function_random_decimal(self):
        """Test if the function resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('rand', 1.2)
        self.assertEqual(self.error_message.get('use integer'),
                         str(exc.exception))
