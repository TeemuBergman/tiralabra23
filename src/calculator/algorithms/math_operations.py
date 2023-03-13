"""Math Operations class."""

import math
import random
from decimal import Decimal, getcontext

# Custom classes
from .error_handling import ErrorMessages, OperationError


class MathOperations:  # pylint: disable=too-few-public-methods
    """This class handles all the mathematical operations."""

    def __init__(self):
        self.error_message = ErrorMessages()

        # Set Decimal precision
        getcontext().prec = 32

        self.arithmetic = {
            '+': self._perform_add,
            '-': self._perform_subtraction,
            '*': self._perform_multiplication,
            '/': self._perform_division,
            '^': self._perform_exponentitation,
            '%': self._perform_modulo
        }

        self.functions = {
            'sinr': self._perform_sinr,
            'cosr': self._perform_cosr,
            'tanr': self._perform_tanr,
            'sind': self._perform_sind,
            'cosd': self._perform_cosd,
            'tand': self._perform_tand,
            'sqrt': self._perform_sqrt,
            'log':  self._perform_log,
            'ln':   self._perform_ln,
            'rand': self._perform_random,
            'fact': self._perform_factorial
        }

        self.result = None

    def perform_on(self, operand: str, value_1: Decimal = None, value_2: Decimal = None) -> Decimal:
        """Perform calculations with given operators, functions or constants
        on 0-2 values {None, Decimal}.

        Time complexity: O(1).

        Args:
            operand (str): Representing the desired operator, function or constant.
            value_1 (Decimal): The first value to be perform calculation on.
            value_2 (Decimal): The second value to be perform calculation  on.

        Returns:
            result (Decimal): The result of the operation, as a float.

        Raises:
            OperationError: on invalid or missing operator or function.
            OperationError: If divide by zero.
            OperationError: If square root operation has value smaller than zero.
            OperationError: If logarithm operation has value smaller than zero.
        """
        # Process functions
        if operand in self.functions:
            try:
                self.functions[operand](value_1)
            except TypeError as exc:
                raise OperationError(self.error_message.get('missing value')) from exc

        # Process arithmetic operations
        elif operand in self.arithmetic:
            try:
                self.arithmetic[operand](value_1, value_2)
            except TypeError as exc:
                raise OperationError(self.error_message.get('missing value')) from exc

        # Given expression is invalid
        else:
            raise OperationError(self.error_message.get('missing operand'))

        # Return the calculation result
        return Decimal(self.result)

    # ARITHMETIC

    def _perform_add(self, value_1, value_2) -> None:
        self.result = value_1 + value_2

    def _perform_subtraction(self, value_1, value_2) -> None:
        self.result = value_1 - value_2

    def _perform_multiplication(self, value_1, value_2) -> None:
        self.result = value_1 * value_2

    def _perform_division(self, value_1, value_2) -> None:
        if value_2 == 0:
            raise OperationError(self.error_message.get('division by zero'))

        self.result = value_1 / value_2

    def _perform_exponentitation(self, value_1, value_2) -> None:
        self.result = value_1 ** value_2

    def _perform_modulo(self, value_1, value_2) -> None:
        self.result = value_1 % value_2

    # FUNCTIONS

    def _perform_sinr(self, value_1) -> None:
        self.result = math.sin(value_1)

    def _perform_cosr(self, value_1) -> None:
        self.result = math.cos(value_1)

    def _perform_tanr(self, value_1) -> None:
        self.result = math.tan(value_1)

    def _perform_sind(self, value_1) -> None:
        self.result = math.sin(math.radians(value_1))

    def _perform_cosd(self, value_1) -> None:
        self.result = math.cos(math.radians(value_1))

    def _perform_tand(self, value_1) -> None:
        self.result = math.tan(math.radians(value_1))

    def _perform_sqrt(self, value_1) -> None:
        if value_1 <= 0:
            raise OperationError(self.error_message.get('square root'))

        self.result = Decimal(value_1).sqrt()

    def _perform_log(self, value_1) -> None:
        if value_1 <= 0:
            raise OperationError(self.error_message.get('logarithm'))

        self.result = Decimal(value_1).log10()

    def _perform_ln(self, value_1) -> None:
        if value_1 <= 0:
            raise OperationError(self.error_message.get('logarithm'))

        self.result = Decimal(value_1).ln()

    def _perform_factorial(self, value_1) -> None:
        if value_1 <= 0:
            raise OperationError(self.error_message.get('factorial negative'))

        if '.' in str(value_1):
            raise OperationError(self.error_message.get('factorial decimal'))

        self.result = math.factorial(int(value_1))

    def _perform_random(self, value_1) -> None:
        if value_1 <= 0:
            raise OperationError(self.error_message.get('random'))

        # Check if value is a integer or has a fractional part
        if '.' in str(value_1):
            self.result = random.uniform(0.0, float(value_1))
        else:
            self.result = random.randint(0, int(value_1))
