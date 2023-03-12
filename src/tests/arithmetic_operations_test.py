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
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('+', 1, 2)
        self.assertEqual(result, 3.0)

    def test_basic_subtraction_1(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('-', 1, 2)
        self.assertEqual(result, -1.0)

    def test_basic_subtraction_2(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('-', 2, 1)
        self.assertEqual(result, 1.0)

    def test_basic_multiplication(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('*', 1, 2)
        self.assertEqual(result, 2.0)

    def test_basic_division_1(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('/', 1, 2)
        self.assertEqual(result, 0.5)

    def test_basic_division_2(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('/', 2, 1)
        self.assertEqual(result, 2.0)

    def test_basic_exponentitation(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('^', 1, 2)
        self.assertEqual(result, 1.0)

    def test_negative_integers(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('-', -1, -2)
        self.assertEqual(result, 1.0)

    def test_negative_float_2(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('-', -1.6, -2.2)
        self.assertAlmostEqual(result, 0.6)

    def test_negative_float_2(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('+', -0.5365729180004349, 0.5365729180004349)
        self.assertAlmostEqual(result, 0)

    def test_negative_float_3(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('/', -0.5365729180004349, 0.5365729180004349)
        self.assertAlmostEqual(result, -1)

    def test_negative_float_3(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('*', 2.6326235723264269, -0.5365729180004349)
        self.assertAlmostEqual(float(result), -1.41259451219992)

    def test_modulo_1(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('%', 12, 2.4)
        self.assertAlmostEqual(result, 0)

    def test_modulo_2(self):
        """Test if the class returns correct answer with given operator and values."""
        result = self.operations.perform_on('%', 12, 5)
        self.assertAlmostEqual(result, 2)

    # FUNCTIONS

    def test_function_sine_radians(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('sinr', 12)
        self.assertAlmostEqual(result, -0.5365729180004349)

    def test_function_sine_degrees(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('sind', 12)
        self.assertAlmostEqual(result, 0.20791169081775934)

    def test_function_cosine_radians(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('cosr', 12)
        self.assertAlmostEqual(result, 0.8438539587324921)

    def test_function_cosine_degrees(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('cosd', 12)
        self.assertAlmostEqual(result, 0.9781476007338057)

    def test_function_tangent_radians(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('tanr', 12)
        self.assertAlmostEqual(result, -0.6358599286615808)

    def test_function_tangent_degrees(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('tand', 12)
        self.assertAlmostEqual(result, 0.21255656167002213)

    def test_function_square_root(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('sqrt', 12)
        self.assertAlmostEqual(float(result), 3.4641016151377544)

    def test_function_logarithm_1(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('log', 12)
        self.assertAlmostEqual(float(result), 1.0791812460476249)

    def test_function_logarithm_2(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('ln', 12)
        self.assertAlmostEqual(float(result), 2.4849066497880004)

    def test_function_random_integer(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('rand', 200)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 200)

    def test_function_random_decimal(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('rand', 20.5)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 20.5)

    def test_function_factorial_1(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('fact', 12)
        self.assertAlmostEqual(result, 479001600)

    # EXCEPTIONS

    def test_division_by_zero(self):
        """Test if the class can divide with zero"""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('/', 1, 0)
        self.assertEqual(self.error_message.get('division by zero'),
                         str(exc.exception))

    def test_no_operand(self):
        """Test if the class works with no operator at all."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('', 0)
        self.assertEqual(self.error_message.get('missing operand'),
                         str(exc.exception))

    def test_invalid_operator_1(self):
        """Test if the class resolves invalid operator to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('&', 1, 0)
        self.assertEqual(self.error_message.get('missing operand'),
                         str(exc.exception))

    def test_invalid_operator_2(self):
        """Test if the class resolves invalid operator to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('s', 4, 4)
        self.assertEqual(self.error_message.get('missing operand'),
                         str(exc.exception))

    def test_function_sine_radians_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('sinr')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_sine_degrees_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('sind')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_cosine_radians_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('cosr')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_cosine_degrees_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('cosd')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_tangent_radians_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('tanr')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_tangent_degrees_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('tand')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_logarithm_no_value_1(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('log')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_logarithm_no_value_2(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('ln')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_logarithm_negative_1(self):
        """Test if the class resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('log', -4)
        self.assertEqual(self.error_message.get('logarithm'),
                         str(exc.exception))

    def test_function_logarithm_negative_2(self):
        """Test if the class resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('ln', -4)
        self.assertEqual(self.error_message.get('logarithm'),
                         str(exc.exception))

    def test_function_square_root_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('sqrt')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_square_root_negative(self):
        """Test if the class resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('sqrt', -4)
        self.assertEqual(self.error_message.get('square root'),
                         str(exc.exception))

    def test_function_negation_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('-')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_operation_addition_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('+')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_operation_subtraction_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('-')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_operation_multiplication_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('*')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_operation_division_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('/')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_operation_exponentitation_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('^')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_random_no_value(self):
        """Test if the class handles errors on functions correctly."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('rand')
        self.assertEqual(self.error_message.get('missing value'),
                         str(exc.exception))

    def test_function_random_negative(self):
        """Test if the class resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('rand', -4)
        self.assertEqual(self.error_message.get('random'),
                         str(exc.exception))

    def test_function_factorial_negative(self):
        """Test if the class resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('fact', -4)
        self.assertEqual(self.error_message.get('factorial negative'),
                         str(exc.exception))

    def test_function_factorial_decimal(self):
        """Test if the class resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('fact', 1.2)
        self.assertEqual(self.error_message.get('factorial decimal'),
                         str(exc.exception))
