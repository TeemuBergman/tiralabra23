class Calculation:
    """A class for storing values for different operations."""

    def __init__(self, expression: str, variables: str):
        """
        Initialize an instance of a class that represents a mathematical expression.

        Args:
            expression (str): A string representing the mathematical expression, with or without variables.
            variables (str): A string containing the variables used in the expression.
        """

        from decimal import Decimal

        # Modify given expression
        self.expression = self._remove_spaces(expression)
        self.expression = self._convert_dot_to_comma(self.expression)
        self.expression = self._convert_to_lowercase(self.expression)

        # Modify given variables
        if variables:
            self.variables = self._remove_spaces(variables)
            self.variables = self._convert_to_lowercase(self.variables)
            # Add variables to a dictionary and process expression with them
            self.variables = self._variables_to_dictionary(self.variables)
            self._introduce_variables()
        else:
            self.variables = {}

        # For storing RPN and result
        self.rpn = ''
        self.result = Decimal()

    def _remove_spaces(self, string: str) -> str:
        """Remove spaces from given string."""
        return string.replace(' ', '')

    def _convert_dot_to_comma(self, string: str) -> str:
        """Convert commas to dots in given string."""
        return string.replace(',', '.')

    def _convert_to_lowercase(self, string: str) -> str:
        """Convert given string to lowercase."""
        return string.lower()

    def _introduce_variables(self) -> None:
        """Replace variables in an expression with values from a dictionary."""

        for key in self.variables:
            self.expression = self.expression.replace(key, self.variables[key])

    def _variables_to_dictionary(self, variables: str) -> dict:
        """
        Convert a string of variables to a dictionary.

        Args:
            variables (str): A string of variables.

        Returns:
            dict: A dictionary representation of the variables string.
        """

        return dict([variable.strip().split('=') for variable in variables.split(',')])
