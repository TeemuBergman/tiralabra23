"""Arithmetic Operations class."""

import math
from decimal import Decimal, DivisionByZero

# Custom classes
from algorithms.error_handling import OperationError


class ArithmeticOperations:
    """This class handles all arithmetic operations."""

    def __init__(self):
        self.result = None

    def perform_on(self, operator: str, value_1: float, value_2 = None) -> Decimal:
        """
        Perform basic arithmetic operations on two values.

        Args:
            operator (str): The symbol representing the desired operation (+, -, *, /, or ^).
            value_1 (float): The first value to be operated on.
            value_2 (float): The second value to be operated on.

        Returns:
            float: The result of the operation, as a float.

        Raises:
            ValueError: If the operator is not found, if a division by zero occurs,
                or if an overflow occurs.
        """
        # Check that there is an operator
        if not operator:
            raise OperationError("Operator missing!")

        # Convert operator to lower case, for function names (sin, cos, tan)
        operator = operator.lower()

        # Convert the values to Decimal objects to ensure decimal precision
        value_1 = Decimal(value_1)
        if value_2:
            value_2 = Decimal(value_2)

        # Perform arithmetics
        if operator == '+':
            self.result = value_1 + value_2
        elif operator == '-':
            self.result = value_1 - value_2
        elif operator == '*':
            self.result = value_1 * value_2
        elif operator == '/':
            # If a division by zero occurs, raise a ValueError with an error message
            try:
                self.result = value_1 / value_2
            except DivisionByZero as exc:
                raise OperationError("Division by zero!") from exc
        elif operator == '^':
            self.result = value_1 ** value_2
        elif operator == 'sinr':
            self.result = self.perform_sine(value_1)
        elif operator == 'cosr':
            self.result = self.perform_cosine(value_1)
        elif operator == 'tanr':
            self.result = self.perform_tangent(value_1)
        elif operator == 'sqr':
            self.result = self.perform_square_root(value_1)
        elif operator == 'log':
            self.result = self.perform_logarithm(value_1)
        else:
            print(operator, value_1, value_2)
            raise OperationError("Invalid operator/variable!")

        # Return the operation result
        return self.result

    def perform_sine(self, value) -> Decimal:
        return Decimal(math.sin(value))

    def perform_cosine(self, value) -> Decimal:
        return Decimal(math.cos(value))

    def perform_tangent(self, value) -> Decimal:
        return Decimal(math.tan(value))

    def perform_square_root(self, value) -> Decimal:
        return Decimal(math.sqrt(value))

    def perform_logarithm(self, value) -> Decimal:
        return Decimal(math.log(value))
