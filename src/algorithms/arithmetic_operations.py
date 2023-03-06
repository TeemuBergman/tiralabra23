"""Arithmetic Operations class."""

import math
from decimal import Decimal

# Custom classes
from .error_handling import OperationError


class ArithmeticOperations:
    """This class handles all arithmetic arithmetic."""

    def __init__(self):
        self.arithmetic = {
            '+':    self._perform_add,
            '-':    self._perform_subtraction,
            '*':    self._perform_multiplication,
            '/':    self._perform_division,
            '^':    self._perform_exponentitation
        }

        self.functions = {
            'sinr': self._perform_sinr,
            'cosr': self._perform_cosr,
            'tanr': self._perform_tanr,
            'sind': self._perform_sind,
            'cosd': self._perform_cosd,
            'tand': self._perform_tand,
            'sqrt': self._perform_sqrt,
            'log':  self._perform_log
        }

        self.result = None

    def perform_on(self, operator: str, value_1: Decimal, value_2: Decimal = None) -> Decimal:
        """
        Perform various mathematical operations.

        Args:
            operator (str): The symbol representing the desired operation (+, -, *, /, or ^).
            value_1 (Decimal): The first value to be operated on.
            value_2 (Decimal): The second value to be operated on.

        Returns:
            result (Decimal): The result of the operation, as a float.

        Raises:
            OperationError: on invalid or missing operator or function.
            OperationError: If divide by zero.
            OperationError: If square root operation has value smaller than zero.
            OperationError: If logarithm operation has value smaller than zero.
        """
        # Perform arithmetics with given values and operator
        if operator in self.functions:
            self.functions[operator](value_1)
        elif operator in self.arithmetic:
            self.arithmetic[operator](value_1, value_2)
        else:
            raise OperationError("Error: Invalid or missing operator or function!")

        # Return the operation result
        return self.result

    # ARITHMETIC

    def _perform_add(self, value_1, value_2) -> None:
        self.result = Decimal(value_1 + value_2)

    def _perform_subtraction(self, value_1, value_2) -> None:
        self.result = Decimal(value_1 - value_2)

    def _perform_multiplication(self, value_1, value_2) -> None:
        self.result = Decimal(value_1 * value_2)

    def _perform_division(self, value_1, value_2) -> None:
        try:
            self.result = Decimal(value_1 / value_2)
        except ZeroDivisionError as exc:
            raise OperationError("Error: Division by zero!") from exc

    def _perform_exponentitation(self, value_1, value_2) -> None:
        self.result = Decimal(value_1 ** value_2)

    # FUNCTIONS

    def _perform_sinr(self, value_1) -> None:
        self.result = Decimal(math.sin(value_1))

    def _perform_cosr(self, value_1) -> None:
        self.result = Decimal(math.cos(value_1))

    def _perform_tanr(self, value_1) -> None:
        self.result = Decimal(math.tan(value_1))

    def _perform_sind(self, value_1) -> None:
        self.result = Decimal(math.sin(math.radians(value_1)))

    def _perform_cosd(self, value_1) -> None:
        self.result = Decimal(math.cos(math.radians(value_1)))

    def _perform_tand(self, value_1) -> None:
        self.result = Decimal(math.tan(math.radians(value_1)))

    def _perform_sqrt(self, value_1) -> None:
        if value_1 < 0:
            raise OperationError('Error: Square root operation has value smaller than zero!')
        self.result = Decimal(math.sqrt(value_1))

    def _perform_log(self, value_1) -> None:
        if value_1 < 0:
            raise OperationError('Error: Logarithm operation has value smaller than zero!')
        self.result = Decimal(math.log(value_1))
