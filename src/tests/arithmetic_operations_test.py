"""Tests for Arithmetic Operations class."""

import unittest

# Custom classes
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
        result = self.operations.perform_on('-', float(1.6), float(2.2))
        self.assertAlmostEqual(float(result), -0.6000000000000000888178419700)

    # FUNCTIONS

    def test_function_sine(self):
        """Test if the function calculates function 'sin(12)."""
        result = self.operations.perform_on('sinr', 12)
        self.assertAlmostEqual(float(result), -0.5365729180004349)

    def test_function_cosine(self):
        """Test if the function calculates function 'cos(12)."""
        result = self.operations.perform_on('cosr', 12)
        self.assertAlmostEqual(float(result), 0.8438539587324921)

    def test_function_tangent(self):
        """Test if the function calculates function 'tan(12)."""
        result = self.operations.perform_on('tanr', 12)
        self.assertAlmostEqual(float(result), -0.6358599286615808)

    # CATCH EXCEPTIONS

    def test_division_by_zero(self):
        """Test if the function can divide with zero"""
        with self.assertRaises(ValueError) as exc:
            self.operations.perform_on('/', 1, 0)
        self.assertEqual("Division by zero!", str(exc.exception))

    def test_no_operator(self):
        """Test if the function works with no operator."""
        with self.assertRaises(ValueError) as exc:
            self.operations.perform_on('', 0)
        self.assertEqual("Operator missing!", str(exc.exception))

    def test_wrong_symbols(self):
        """Test if the function resolves erroneous symbol to error."""
        with self.assertRaises(ValueError) as exc:
            self.operations.perform_on('%', 1, 0)
        self.assertEqual("Invalid operator!", str(exc.exception))
