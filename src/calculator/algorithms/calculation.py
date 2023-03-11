"""Calculation class."""

# Custom classes
from utils.error_handling import ErrorMessages, VariableError, ExpressionError
from .constants import Constants


class Calculation:  # pylint: disable=too-few-public-methods
    """A class for storing values for different operations."""

    def __init__(self):
        self._error_messages = ErrorMessages()
        self._constants = Constants()
        # Original values
        self.expression = ''
        self.variables = ''
        # Variables for storing RPN and result
        self.result_rpn = None
        self.result = None
        # Memory
        self.memory = ''

    def new(self, expression: str, variables: str = None):
        """This adds constants and user given variables to expression,
           before its sent to Shunting Yard algorithm.

        Args:
            expression (str): A string representing the mathematical expression.
            variables (str): A string of variables.
        """
        # Handle expression
        if expression:
            # Modify given expression
            self.expression = self._remove_spaces(expression)
            self.expression = self._convert_dot_to_comma(self.expression)
            self.expression = self._convert_to_lowercase(self.expression)
            # Process given constants to values in expression
            self._introduce_constants()
        else:
            raise ExpressionError(self._error_messages.get('expression not found'))

        # Handle variables
        if variables:
            # Clean given variables for whitespace and uppercase characters
            self.variables = self._remove_spaces(variables)
            self.variables = self._convert_to_lowercase(self.variables)
            # Add variables_dictionary to a dictionary and process expression with them
            self.variables = self._variables_to_dictionary(self.variables)
            # Process given variables to given expression
            self._introduce_variables(self.variables)
        else:
            self.variables = ''

        return self

    def _remove_spaces(self, string: str) -> str:
        """Remove spaces from given string."""
        return string.replace(' ', '')

    def _convert_dot_to_comma(self, string: str) -> str:
        """Convert commas to dots in given string."""
        return string.replace(',', '.')

    def _convert_to_lowercase(self, string: str) -> str:
        """Convert given string to lowercase."""
        return string.lower()

    def _variables_to_dictionary(self, variables: str) -> dict:
        """Convert a string of variables to a dictionary.

        Args:
            variables (str): A string of variables.
        """
        variables_list = variables.split(',')
        variables_dictionary = {}

        for variable in variables_list:
            # Split string to key and value
            try:
                key, value = variable.split('=')
            except ValueError as exc:
                raise VariableError(self._error_messages.get('no value')) from exc

            # Check that there is a value
            if not value:
                raise VariableError(self._error_messages.get('no value'))

            # Check that value is a rational number and add it to dictionary
            try:
                float(value)
            except ValueError as exc:
                raise VariableError(self._error_messages.get('not a variable')) from exc
            else:
                variables_dictionary[key] = value

        return variables_dictionary

    def _introduce_constants(self) -> None:
        """Replace given constant names with values."""
        # Introduce mathematical constants
        for key, value in self._constants.mathematical.items():
            self.expression = self.expression.replace(key, value)

    def _introduce_variables(self, variables_dictionary: dict) -> None:
        """Replace given user variable names with values."""
        # Introduce user variables
        for key, value in variables_dictionary.items():
            self.expression = self.expression.replace(key, value)

    # MEMORY OPERATIONS

    def save_to_memory(self) -> None:
        """..."""
        self.memory = self.result

    def add_to_memory(self) -> None:
        """..."""
        self.memory += self.result

    def subtract_from_memory(self) -> None:
        """..."""
        self.memory -= self.result

    def clear_memory(self) -> None:
        """..."""
        self.memory = 0
