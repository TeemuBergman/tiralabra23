class Calculation:
    """
    Lorem
    """

    def __init__(self, expression: str, variables: str):
        """
        :param expression:
        :type expression:
        :param variables:
        :type variables:
        """
        self.variables = variables
        self.variables_dict = self._variables_to_dictionary(self.variables)
        self.expression_original = expression
        self.expression = self._introduce_variables(
            self.expression_original, self.variables_dict)
        self.rpn = ''
        self.result = None

    def _introduce_variables(self, expression: str, variables: dict) -> str:
        """
        Replace variables in an expression with values from a dictionary.

        Args:
            expression (str): The expression to replace variables in.
            variables (dict): A dictionary of variable names (as keys) and values.

        Returns:
            str: The expression with variables substituted by values from the dictionary.
        """

        for key, value in variables.items():
            expression = expression.replace(key, value)

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

        return dict(variable.split("=") for variable in variables.split(","))
