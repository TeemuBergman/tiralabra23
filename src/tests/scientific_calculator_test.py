"""Tests for Scientific Calculator class."""

import unittest

# Custom classes
from utils.error_handling import ErrorMessages, ExpressionError, VariableError, OperationError
from calculator.algorithms.calculation import Calculation
from calculator.scientific_calculator import ScientificCalculator


class TestScientificCalculator(unittest.TestCase):
    """Tests for ScientificCalculator class."""

    def setUp(self):
        self.error_message = ErrorMessages()
        self.calculation = Calculation()
        self.scientific_calculator = ScientificCalculator()

    # BASIC TESTS

    def test_basic_addition(self):
        """Test if the class returns correct answer with simple input."""
        expression = '1+2'
        response = self.scientific_calculator.calculate(expression)
        self.assertEqual(response, 3)

    def test_basic_subtraction(self):
        """Test if the class returns correct answer with simple input."""
        expression = '1-2'
        response = self.scientific_calculator.calculate(expression)
        self.assertEqual(response, -1)

    def test_basic_multiplication(self):
        """Test if the class returns correct answer with simple input."""
        expression = '2*2'
        response = self.scientific_calculator.calculate(expression)
        self.assertEqual(response, 4)

    def test_basic_division(self):
        """Test if the class returns correct answer with simple input."""
        expression = '2/2'
        response = self.scientific_calculator.calculate(expression)
        self.assertEqual(response, 1)

    def test_basic_exponentitation(self):
        """Test if the class returns correct answer with simple input."""
        expression = '2^8'
        response = self.scientific_calculator.calculate(expression)
        self.assertEqual(response, 256)

    # FUNCTIONS

    def test_functions_1(self):
        """Test if the class returns correct answer with simple input."""
        expression = 'sinr(sqrt(12))*23'
        result = self.scientific_calculator.calculate(expression)
        self.assertAlmostEqual(float(result), -7.289784753629491631521375439)

    def test_functions_2(self):
        """Test if the class returns correct answer with simple input."""
        expression = 'sqrt(6^64)'
        result = self.scientific_calculator.calculate(expression)
        self.assertAlmostEqual(float(result), 7.958661109946401e+24)

    # EXCEPTIONS

    def test_empty_input(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.scientific_calculator.calculate('')
        self.assertEqual(self.error_message.get('expression not found'),
                         str(exc.exception))

    def test_division_by_zero(self):
        """Test if the function can divide with zero"""
        with self.assertRaises(OperationError) as exc:
            self.scientific_calculator.calculate('1/0')
        self.assertEqual(self.error_message.get('division by zero'),
                         str(exc.exception))

    def test_invalid_operator_1(self):
        """Test if the function resolves invalid operator to error."""
        with self.assertRaises(ExpressionError) as exc:
            self.scientific_calculator.calculate('1%1')
        self.assertEqual(self.error_message.get('not a valid expression'),
                         str(exc.exception))

    def test_invalid_expression_1(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.scientific_calculator.calculate('(1/2)*(1/2')
        self.assertEqual(self.error_message.get('not a valid expression'),
                         str(exc.exception))

    def test_invalid_expression_2(self):
        """Test if the function raises ExpressionError with invalid input."""
        with self.assertRaises(ExpressionError) as exc:
            self.scientific_calculator.calculate('sinr12')
        self.assertEqual(self.error_message.get('not a valid expression'),
                         str(exc.exception))

    def test_invalid_variable_1(self):
        """Test if the function raises VariableError with invalid input."""
        with self.assertRaises(VariableError) as exc:
            self.scientific_calculator.calculate('x*2', 'x=,')
        self.assertEqual(self.error_message.get('no value'),
                         str(exc.exception))

    def test_invalid_variable_2(self):
        """Test if the function raises VariableError with invalid input."""
        with self.assertRaises(VariableError) as exc:
            self.scientific_calculator.calculate('x*2', 'x=%')
        self.assertEqual(self.error_message.get('not a variable'),
                         str(exc.exception))

    def test_invalid_variable_3(self):
        """Test if the function raises VariableError with invalid input."""
        with self.assertRaises(VariableError) as exc:
            self.scientific_calculator.calculate('x*2', 'x=1,y')
        self.assertEqual(self.error_message.get('no value'),
                         str(exc.exception))

    def test_invalid_variable_4(self):
        """Test if the function resolves negative values to error."""
        with self.assertRaises(ExpressionError) as exc:
            self.scientific_calculator.calculate('x+1', '')
        self.assertEqual(self.error_message.get('not a valid expression'),
                         str(exc.exception))

    def test_negative_square_root(self):
        """Test if the function resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.scientific_calculator.calculate('sqrt(x)', 'x=-4')
        self.assertEqual(self.error_message.get('square root'),
                         str(exc.exception))

    def test_negative_logarithm(self):
        """Test if the function resolves negative values to error."""
        with self.assertRaises(OperationError) as exc:
            self.scientific_calculator.calculate('log(x)', 'x=-4')
        self.assertEqual(self.error_message.get('logarithm'),
                         str(exc.exception))
