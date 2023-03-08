"""Postfix Evaluator class."""

from decimal import Decimal, InvalidOperation

# Custom classes
from .error_handling import ExpressionError
from .calculation import Calculation
from .arithmetic_operations import ArithmeticOperations


class PostfixEvaluator:
    """
    Postfix evaluator takes an postfix expressions as input and evaluates it.
    """

    def __init__(self):
        self.operations = ArithmeticOperations()
        self.symbols = []
        self.stack = []
        self.result = Decimal()

    def evaluate(self, calculation: Calculation) -> None:
        """
        Evaluate a postfix expression.

        Args:
            calculation (Calculation): Object contains the RPN expression to be evaluated.

        Returns:
            Decimal: The result of the expression.

        Raises:
            ValueError: If there are not enough values in the expression to perform_on
                the arithmetic operation.complete
        """
        # Check if the input expression is empty
        if not calculation.result_rpn:
            raise ExpressionError("Error: Expression not found!")

        # Split the input expression into symbols using whitespace as a separator
        self.symbols = calculation.result_rpn.split(' ')

        # Iterate over each symbol in the expression
        for step, symbol in enumerate(self.symbols):
            # If symbol has a length > 1 and its second character is a numeric
            # then append it to stack
            if len(symbol) > 1 and symbol[1].isnumeric():
                try:
                    # Convert the symbol to a Decimal and push it into the stack
                    self.stack.append(Decimal(symbol))
                except InvalidOperation as exc:
                    raise ExpressionError('Error: Not in decimal format, too many dots!') from exc

            # If the symbol starts with a digit append it to stack
            elif symbol[0].isnumeric():
                try:
                    # Convert the symbol to a Decimal and push it into the stack
                    self.stack.append(Decimal(symbol))
                except InvalidOperation as exc:
                    raise ExpressionError('Error: Not in decimal format, too many dots!') from exc

            # If the symbol is NaN, then it must bea an operator
            else:
                if symbol in self.operations.functions:
                    # If operator is a function
                    value_2 = None
                    value_1 = self.stack.pop()
                elif symbol in self.operations.arithmetic and len(self.stack) >= 2:
                    # Pop the last two values from the stack
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()
                else:
                    raise ExpressionError('Error: Not a valid expression!')

                # Perform the operation with the symbol and the two values
                result = self.operations.perform_on(symbol, value_1, value_2)
                # Push the result onto the stack
                self.stack.append(result)

        # The final result is the only value remaining on the stack
        calculation.result = self.stack.pop()
