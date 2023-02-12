from algorithms.shunting_yard import shunting_yard
from algorithms.postfix_evaluator import postfix_evaluator


class ScientificCalculator:
    """
    A scientific calculator that can evaluate expressions.

    The calculator can handle variables in the expression,
    which can be provided as a comma-separated string of key-value pairs.
    """

    def __init__(self, expression, variables=None):
        """
        Initialize the scientific calculator.

        Args:
            expression (str): The expression to evaluate.
            variables (str, optional): A string of variables to use in the expression.
        """
        self.expression = expression
        self.variables = self.variables_to_dictionary(variables)

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

    def calculate(self):
        """
        Evaluate the expression provided in the constructor.

        Returns:
            float: The result of evaluating the expression.
        """
        # Use the shunting yard algorithm to convert the expression to reverse
        # polish notation
        result_rpn = shunting_yard(self.expression, self.variables)
        # Use the postfix evaluator to calculate the result from the reverse
        # polish notation
        result = postfix_evaluator(result_rpn)
        return result
