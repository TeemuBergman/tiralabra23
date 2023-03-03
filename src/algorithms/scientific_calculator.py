"""Scientific Calculator class."""

from decimal import Decimal

# Custom classes
from algorithms.postfix_evaluator import PostfixEvaluator
from algorithms.shunting_yard import ShuntingYard
from algorithms.calculation import Calculation


class ScientificCalculator:
    """
    A scientific calculator that can evaluate different mathematical expressions.

    The calculator can handle variables in the expression,
    which can be provided as a comma-separated string of key-value pairs.
    """

    def __init__(self):
        self.shunting_yard = ShuntingYard()
        self.postfix_evaluator = PostfixEvaluator()
        self.result_rpn = ''
        self.result = Decimal()

    def calculate(self, expression: str, variables=None) -> Decimal:
        """
        Evaluate the expression provided in the constructor.

        Args:
            expression (str): A string representing the mathematical expression, with or without variables.
            variables (str): A string containing the variables used in the expression.

        Returns:
            Decimal: The result of evaluating the expression.
        """

        # Create new calculation object
        calculation = Calculation(expression, variables)

        # Use the shunting yard algorithm to convert
        # the expression to a reverse polish notation
        self.result_rpn = self.shunting_yard.convert(calculation)

        # Use the postfix evaluator to calculate
        # the result from the reverse polish notation
        self.result = self.postfix_evaluator.evaluate(self.result_rpn)

        return self.result
