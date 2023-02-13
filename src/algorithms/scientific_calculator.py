from algorithms.shunting_yard import shunting_yard
from algorithms.postfix_evaluator import postfix_evaluator


class ScientificCalculator:
    """
    A scientific calculator that can evaluate expressions.

    The calculator can handle variables in the expression,
    which can be provided as a comma-separated string of key-value pairs.
    """

    def calculate(self, expression, variables=None):
        """
        Evaluate the expression provided in the constructor.

        Returns:
            float: The result of evaluating the expression.
        """

        # Convert a string of variables to dictionary of variables
        if variables:
            variables = self.variables_to_dictionary(variables)

        # Use the shunting yard algorithm to convert the expression to
        # reverse polish notation
        result_rpn = shunting_yard(expression, variables)

        # Use the postfix evaluator to calculate the result from the
        # reverse polish notation
        result = postfix_evaluator(result_rpn)
        return result

    def variables_to_dictionary(self, variables):
        """
        Convert a string of variables to a dictionary.

        Args:
            variables (str, optional): A string of variables.

        Returns:
            dict: A dictionary representation of the variables string.
        """

        if not variables:
            return None
        return dict(variable.split("=") for variable in variables.split(","))
