"""Arithmetic Operations class."""

import math
from decimal import Decimal, DivisionByZero

# Custom classes
from algorithms.error_handling import OperationError


class ArithmeticOperations:
    """This class handles all arithmetic operations."""

    def __init__(self):
        self.functions = ['sinr', 'cosr', 'tanr', 'sqrt', 'log']
        self._operations = {
            '+': self._perform_add,
            '-': self._perform_subtraction,
            '*': self._perform_multiplication,
            '/': self._perform_division,
            '^': self._perform_exponentitation,
            'sinr': self._perform_sinr,
            'cosr': self._perform_cosr,
            'tanr': self._perform_tanr,
            'sqrt': self._perform_sqrt,
            'log': self._perform_log
        }
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
            OperationError: If operator or function is not found.
        """
        # Check that there is an (correct) operator
        try:
            self._operations[operator]
        except KeyError as exc:
            raise OperationError("Error: Operator missing or not correct!") from exc

        # Convert the values to Decimal objects to ensure decimal precision
        value_1 = Decimal(value_1)
        if value_2:
            value_2 = Decimal(value_2)

        # Perform arithmetics with given values and operator
        try:
            self._operations[operator](value_1, value_2)
        except ValueError as exc:
            raise OperationError("Error: Invalid operator/function!") from exc

        # Return the operation result
        return self.result

    # OPERATIONS

    def _perform_add(self, value_1, value_2) -> None:
        self.result = value_1 + value_2

    def _perform_subtraction(self, value_1, value_2) -> None:
        self.result = value_1 - value_2

    def _perform_multiplication(self, value_1, value_2) -> None:
        self.result = value_1 * value_2

    def _perform_division(self, value_1, value_2) -> None:
        try:
            self.result = value_1 / value_2
        except DivisionByZero as exc:
            raise OperationError("Error: Division by zero!") from exc

    def _perform_exponentitation(self, value_1, value_2) -> None:
        self.result = value_1 ** value_2

    # FUNCTIONS

    def _perform_sinr(self, value_1, *value_2) -> None:
        self._void(value_2)
        self.result = Decimal(math.sin(value_1))

    def _perform_cosr(self, value_1, *value_2) -> None:
        self._void(value_2)
        self.result = Decimal(math.cos(value_1))

    def _perform_tanr(self, value_1, *value_2) -> None:
        self._void(value_2)
        self.result = Decimal(math.tan(value_1))

    def _perform_sqrt(self, value_1, *value_2) -> None:
        self._void(value_2)
        if value_1 < 0:
            raise OperationError('Error: Square root operation has value smaller than zero!')
        self.result = Decimal(math.sqrt(value_1))

    def _perform_log(self, value_1, *value_2) -> None:
        self._void(value_2)
        if value_1 < 0:
            raise OperationError('Error: Logarithm operation has value smaller than zero!')
        self.result = Decimal(math.log(value_1))

    def _void(self, value) -> None:
        pass
