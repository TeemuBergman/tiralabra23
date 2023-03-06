"""Scientific Calculator class."""

from decimal import Decimal

# Custom classes
from .postfix_evaluator import PostfixEvaluator
from .shunting_yard import ShuntingYard
from .calculation import Calculation


class ScientificCalculator:
    """
    A scientific calculator that can evaluate different mathematical expressions.

    The calculator can handle variables in the expression,
    which can be provided as a comma-separated string of key-value pairs.
    """

    def __init__(self):
        self.calculation = None
        self.shunting_yard = ShuntingYard()
        self.postfix_evaluator = PostfixEvaluator()

    def calculate(self, expression: str, variables = None) -> Decimal:
        """
        Evaluate the expression provided in the constructor.

        Args:
            expression (str): A string representing the mathematical expression,
            with or without variables.
            variables (str): A string containing the variables used in the expression.

        Returns:
            Decimal: The result of evaluating the expression.
        """
        # Create a new calculation object
        self.calculation = Calculation().new(expression, variables)

        # Use the Shunting Yard algorithm to convert
        # the expression to a Reverse Polish Notation
        self.shunting_yard.convert(self.calculation)

        # Use the postfix evaluator to calculate
        # the final result from the Reverse Polish Notation
        self.postfix_evaluator.evaluate(self.calculation)

        return self.calculation.result
