"""Tests for Arithmetic Operations class."""

import unittest

# Custom classes
from algorithms.error_handling import OperationError
from algorithms.arithmetic_operations import ArithmeticOperations


class TestArithmeticOperations(unittest.TestCase):
    """Tests for ArithmeticOperations class."""

    def setUp(self):
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

    def test_function_sine(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('sinr', 12)
        self.assertAlmostEqual(float(result), -0.5365729180004349)

    def test_function_cosine(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('cosr', 12)
        self.assertAlmostEqual(float(result), 0.8438539587324921)

    def test_function_tangent(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('tanr', 12)
        self.assertAlmostEqual(float(result), -0.6358599286615808)

    def test_function_square_root(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('sqrt', 12)
        self.assertAlmostEqual(float(result), 3.4641016151377544)

    def test_function_logarithm(self):
        """Test if the class evaluates given expression correctly."""
        result = self.operations.perform_on('log', 12)
        self.assertAlmostEqual(float(result), 2.4849066497880004)

    # EXCEPTIONS

    def test_division_by_zero(self):
        """Test if the function can divide with zero"""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('/', 1, 0)
        self.assertEqual('Error: Division by zero!', str(exc.exception))

    def test_no_operator(self):
        """Test if the function works with no operator at all."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('', 0)
        self.assertEqual('Error: Operator missing!', str(exc.exception))

    def test_invalid_operator_1(self):
        """Test if the function resolves invalid operator to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('%', 1, 0)
        self.assertEqual('Error: Invalid operator/function!', str(exc.exception))

    def test_invalid_operator_2(self):
        """Test if the function resolves invalid operator to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('s', 4, 4)
        self.assertEqual('Error: Invalid operator/function!', str(exc.exception))

    def test_negative_square_root(self):
        """Test if the function resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('sqrt', -4, 0)
        self.assertEqual('Error: Square root operation has value smaller than zero!',
                         str(exc.exception))

    def test_negative_logarithm(self):
        """Test if the function resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.operations.perform_on('log', -4, 0)
        self.assertEqual('Error: Logarithm operation has value smaller than zero!',
                         str(exc.exception))
