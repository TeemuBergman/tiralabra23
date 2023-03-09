"""Calculation class."""

# Custom classes
from .constants import Constants
from utils.error_handling import ErrorMessages, VariableError, ExpressionError


class Calculation:
    """A class for storing values for different operations."""

    def __init__(self):
        """
        Initialize an instance of a class that represents a mathematical expression.

        Args:
            expression (str): A string representing the mathematical expression.
            variables (str): A string containing the variables_dictionary used in the expression.
        """
        self._constants = Constants()
        self._error_messages = ErrorMessages()
        # Original values
        self.expression = ''
        self.variables = ''
        # Handled variables
        self.variables_dictionary = {}
        # Variables for storing RPN and result
        self.result_rpn = None
        self.result = None

    def new(self, expression: str, variables: str = None):
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
            self._variables_to_dictionary(self.variables)
            # Process given variables to given expression
            self._introduce_variables()
        else:
            self.variables = ''

        return self

    def _introduce_constants(self) -> None:
        """Replace given constant names with values."""
        # Introduce mathematical constants
        for key, value in self._constants.mathematical.items():
            self.expression = self.expression.replace(key, value)

    def _introduce_variables(self) -> None:
        """Replace given user variable names with values."""
        # Introduce user variables
        for key, value in self.variables_dictionary.items():
            self.expression = self.expression.replace(key, value)

    def _remove_spaces(self, string: str) -> str:
        """Remove spaces from given string."""
        return string.replace(' ', '')

    def _convert_dot_to_comma(self, string: str) -> str:
        """Convert commas to dots in given string."""
        return string.replace(',', '.')

    def _convert_to_lowercase(self, string: str) -> str:
        """Convert given string to lowercase."""
        return string.lower()

    def _variables_to_dictionary(self, variables: str) -> None:
        """
        Convert a string of variables to a dictionary.

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

            # Check that value is a numeral and add it to dictionary
            try:
                float(value)
            except ValueError as exc:
                raise VariableError(self._error_messages.get('not a variable')) from exc
            else:
                variables_dictionary[key] = value

        self.variables_dictionary = variables_dictionary

    # Todo - Is this needed?
    def _clean_output_string(self, value) -> str:
        """Convert given value to a string and modify if it ends at .0"""
        cleaned = str(value)
        # If input value is a decimal with .0 at the end
        if cleaned.endswith('.0'):
            # remove '.0' from end of string
            return cleaned[:-2]
        return cleaned
