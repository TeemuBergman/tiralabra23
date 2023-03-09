"""Postfix Evaluator class."""

from decimal import Decimal, InvalidOperation

# Custom classes
from .error_handling import ErrorMessages, ExpressionError
from .calculation import Calculation
from .arithmetic_operations import ArithmeticOperations


class PostfixEvaluator:
    """
    Postfix evaluator takes a postfix expressions as input and evaluates it.
    """

    def __init__(self):
        self.error_message = ErrorMessages().expression_errors
        self.operations = ArithmeticOperations()
        self.stack = []

    def evaluate(self, calculation: Calculation) -> None:
        """
        Evaluate a postfix expression.

        Args:
            calculation (Calculation): Object contains the RPN expression to be evaluated.

        Raises:
            ValueError: If there are not enough values in the expression to perform_on
                the arithmetic operation.complete
        """
        # Check that expression exists
        if not calculation.result_rpn:
            raise ExpressionError(self.error_message['expression not found'])

        # Split the input expression into symbols using whitespace as a separator
        symbols = calculation.result_rpn.split(' ')

        # Iterate over each symbol in the expression
        for step, symbol in enumerate(symbols):
            # If the symbol starts with a numeral, append it to stack
            if symbol[0].isnumeric():
                try:
                    # Convert the symbol to a Decimal and push it into the stack
                    self.stack.append(Decimal(symbol))
                except InvalidOperation as exc:
                    raise ExpressionError(self.error_message['not a number']) from exc

            # If symbol has a length > 1 and its second character is a numeric,
            # its a negative value and not a negation (that is an operator)
            elif len(symbol) > 1 and symbol[1].isnumeric():
                try:
                    # Convert the symbol to a Decimal and push it into the stack
                    self.stack.append(Decimal(symbol))
                except InvalidOperation as exc:
                    raise ExpressionError(self.error_message['not a number']) from exc

            # If the symbol is not a number, then it must be a operator or a function
            else:
                if symbol in self.operations.constants:
                    # If symbol is a constant, pop nothing
                    value_2 = None
                    value_1 = None
                elif symbol in self.operations.functions:
                    # If symbol is a function, pop only one value
                    value_2 = None
                    value_1 = self.stack.pop()
                elif symbol in self.operations.arithmetic and len(self.stack) >= 2:
                    # If symbol is an operator, pop two values
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()
                else:
                    raise ExpressionError(self.error_message['not valid expression'])

                # Perform the operation with the current symbol and two values {None, rational number}
                result = self.operations.perform_on(symbol, value_1, value_2)
                # Push the result into the stack
                self.stack.append(result)

        # The final result is the only value remaining on the stack
        calculation.result = self.stack.pop()
