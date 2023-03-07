"""Calculation class."""

# Custom classes
from .error_handling import VariableError, ExpressionError


class Calculation:
    """A class for storing values for different operations."""

    def __init__(self):
        """
        Initialize an instance of a class that represents a mathematical expression.

        Args:
            expression (str): A string representing the mathematical expression.
            variables (str): A string containing the variables_dictionary used in the expression.
        """
        # Original values
        self.expression = ''
        self.variables = ''
        self.variables_dictionary = {}
        # Variables for storing RPN and result
        self.result_rpn = ''
        self.result = None

    def new(self, expression: str, variables: str = None):
        if expression:
            # Modify given expression
            self.expression = self._remove_spaces(expression)
            self.expression = self._convert_dot_to_comma(self.expression)
            self.expression = self._convert_to_lowercase(self.expression)
        else:
            raise ExpressionError('Error: Expression not found!')

        # Modify given variables_dictionary
        if variables:
            self.variables = self._remove_spaces(variables)
            self.variables = self._convert_to_lowercase(self.variables)
            # Add variables_dictionary to a dictionary and process expression with them
            self.variables_dictionary = self._variables_to_dictionary(self.variables)
            self._introduce_variables()
        else:
            self.variables = ''

        return self

    def _introduce_variables(self) -> None:
        """Replace variables_dictionary in an expression with values from a dictionary."""
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

    def _variables_to_dictionary(self, variables: str) -> dict:
        """
        Convert a string of variables to a dictionary.

        Args:
            variables (str): A string of variables.

        Returns:
            dict: A dictionary representation of the variables string.
        """
        variables_list = variables.split(',')
        variables_dictionary = {}

        for variable in variables_list:
            # Split string to key and value
            try:
                key, value = variable.split('=')
            except ValueError as exc:
                raise VariableError('Error: Variable(s) with value missing!') from exc

            # Check that there is a value
            if not value:
                raise VariableError(f'Error: Variable \'{key}\' has a missing value!')

            # Check that value is a numeral and add it to dictionary
            try:
                float(value)
            except ValueError as exc:
                raise VariableError(f'Error: Value \'{value}\' is not a number!') from exc
            else:
                variables_dictionary[key] = value

        return variables_dictionary
