from decimal import Decimal

class Calculation:
    """
    A class for storing values for different operations.
    """

    def __init__(self, expression: str, variables: str):
        """
        Initialize an instance of a class that represents a mathematical expression.

        Args:
            expression (str): A string representing the mathematical expression, with or without variables.
            variables (str): A string containing the variables used in the expression.
        """

        self.variables_dict = self._variables_to_dictionary(variables)
        self.expression = self._introduce_variables(
            expression, self.variables_dict)
        self.rpn = ''
        self.result = Decimal

    def _introduce_variables(self, expression: str, variables_dict: dict) -> str:
        """
        Replace variables in an expression with values from a dictionary.

        Args:
            expression (str): The expression to replace variables in.
            variables (dict): A dictionary of variable names (as keys) and values.

        Returns:
            str: The expression with variables substituted by values from the dictionary.
        """

        for key in variables_dict:
            expression = expression.replace(key, variables_dict[key])

        return expression

    def _variables_to_dictionary(self, variables: str) -> dict:
        """
        Convert a string of variables to a dictionary.

        Args:
            variables (str): A string of variables.

        Returns:
            dict: A dictionary representation of the variables string.
        """

        if not variables:
            return {}

        return dict([variable.strip().split('=') for variable in variables.split(',')])
