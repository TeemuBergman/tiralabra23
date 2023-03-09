"""Arithmetic Operations class."""

import math
from decimal import Decimal

# Custom classes
from utils.error_handling import ErrorMessages, OperationError


class ArithmeticOperations:
    """This class handles all arithmetic operations."""

    def __init__(self):
        self.arithmetic = {
            '+': self._perform_add,
            '-': self._perform_subtraction,
            '*': self._perform_multiplication,
            '/': self._perform_division,
            '^': self._perform_exponentitation
        }

        self.functions = {
            '-(': self._perform_negation,
            'sinr': self._perform_sinr,
            'cosr': self._perform_cosr,
            'tanr': self._perform_tanr,
            'sind': self._perform_sind,
            'cosd': self._perform_cosd,
            'tand': self._perform_tand,
            'sqrt': self._perform_sqrt,
            'log':  self._perform_log
        }

        self.constants = {
            'pi': self._return_pi,
            'tau': self._return_tau,
            'phi': self._return_phi,
            'e': self._return_euler
        }

        # Error messages
        self.error_message = ErrorMessages()

        self.result = None

    def perform_on(self, operand: str, value_1: Decimal = None, value_2: Decimal = None) -> Decimal:
        """
        Perform calculations with given operators, functions or constants on 0-2 values {None, Decimal}.

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
        # Check the type of given operand
        if operand in self.constants:
            self.constants[operand]()
        elif operand in self.functions:
            try:
                self.functions[operand](value_1)
            except TypeError as exc:
                raise OperationError(self.error_message.get('missing value')) from exc
        elif operand in self.arithmetic:
            try:
                self.arithmetic[operand](value_1, value_2)
            except TypeError as exc:
                raise OperationError(self.error_message.get('missing value')) from exc
        else:
            raise OperationError(self.error_message.get('missing operand'))

        # Return the calculation result
        return self.result

    # ARITHMETIC

    def _perform_add(self, value_1, value_2) -> None:
        self.result = Decimal(value_1 + value_2)

    def _perform_subtraction(self, value_1, value_2) -> None:
        self.result = Decimal(value_1 - value_2)

    def _perform_multiplication(self, value_1, value_2) -> None:
        self.result = Decimal(value_1 * value_2)

    def _perform_division(self, value_1, value_2) -> None:
        if value_2 == 0:
            raise OperationError(self.error_message.get('division by zero'))
        self.result = Decimal(value_1 / value_2)

    def _perform_exponentitation(self, value_1, value_2) -> None:
        self.result = Decimal(value_1 ** value_2)

    # FUNCTIONS

    def _perform_negation(self, value_1) -> None:
        self.result = Decimal(-value_1)

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
        if value_1 <= 0:
            raise OperationError(self.error_message.get('square root'))
        self.result = Decimal(math.sqrt(value_1))

    def _perform_log(self, value_1) -> None:
        if value_1 <= 0:
            raise OperationError(self.error_message.get('logarithm'))
        self.result = Decimal(math.log(value_1))

    # CONSTANTS

    def _return_pi(self) -> None:
        self.result = Decimal(3.1415926535897932384626433832795028841971693993751058209749445923)

    def _return_tau(self) -> None:
        self.result = Decimal(6.2831853071795864769252867665590057683943387987502116419498891846)

    def _return_phi(self) -> None:
        self.result = Decimal(1.6180339887498948482045868343656381177203091798057628621354486227)

    def _return_euler(self) -> None:
        self.result = Decimal(2.7182818284590452353602874713526624977572470936999595749669676277)