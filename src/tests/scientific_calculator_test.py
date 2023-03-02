import unittest

from algorithms.scientific_calculator import ScientificCalculator


class TestScientificCalculator(unittest.TestCase):
    """Tests for ScientificCalculator class in algorithms.scientific_calculator."""

    def setUp(self):
        self.scientific_calculator = ScientificCalculator()

    # BASIC TESTS

    def test_with_simple_addition(self):
        """Test if the class returns correct answer with simple input."""
        expression = '1+2'
        response = self.scientific_calculator.calculate(expression)
        self.assertEqual(response, 3.0)

    # CATCH EXCEPTIONS

    def test_empty_input(self):
        """Test with empty input."""
        with self.assertRaises(ValueError) as exc:
            self.scientific_calculator.calculate('')
        self.assertEqual("Expression missing!", str(exc.exception))
