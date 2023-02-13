import unittest
from algorithms.basic_operations import basic_operations
from decimal import DivisionByZero


class TestShuntingYard(unittest.TestCase):
    """Tests for shunting_yard function in algorithms.shunting_yard module."""

    def setUp(self):
        self.decimal = DivisionByZero()

    def test_no_operator(self):
        """Test if the function returns None with no operator."""
        result = basic_operations('', 0, 0)
        self.assertEqual(result, None)

    def test_basic_addition(self):
        """Test if the function calculates values '1+2' to a result of 3.0."""
        result = basic_operations('+', 1, 2)
        self.assertEqual(result, 3.0)

    def test_basic_subtraction_1(self):
        """Test if the function calculates values '1-2' to a result of -1.0."""
        result = basic_operations('-', 1, 2)
        self.assertEqual(result, -1.0)

    def test_basic_subtraction_2(self):
        """Test if the function calculates values '2-1' to a result of 1.0."""
        result = basic_operations('-', 2, 1)
        self.assertEqual(result, 1.0)

    def test_basic_multiplication(self):
        """Test if the function calculates values '1*2' to a result of 2.0."""
        result = basic_operations('*', 1, 2)
        self.assertEqual(result, 2.0)

    def test_basic_division_1(self):
        """Test if the function calculates values '1/2' to a result of 0.5."""
        result = basic_operations('/', 1, 2)
        self.assertEqual(result, 0.5)

    def test_basic_division_2(self):
        """Test if the function calculates values '2/1' to a result of 2.0"""
        result = basic_operations('/', 2, 1)
        self.assertEqual(result, 2.0)

    def test_division_by_zero(self):
        """Test if the function divides with zero"""
        with self.assertRaises(ValueError) as exc:
            basic_operations('/', 1, 0)
        self.assertEqual("Division by zero", str(exc.exception))

    def test_basic_exponentitation(self):
        """Test if the function calculates values '1^2' to a result of 1.0."""
        result = basic_operations('^', 1, 2)
        self.assertEqual(result, 1.0)
