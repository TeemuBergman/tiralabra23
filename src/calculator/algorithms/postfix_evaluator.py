"""Postfix Evaluator class."""

from decimal import Decimal, InvalidOperation

# Custom classes
from utils.error_handling import ErrorMessages, ExpressionError
from .calculation import Calculation
from .arithmetic_operations import ArithmeticOperations


class PostfixEvaluator:  # pylint: disable=too-few-public-methods
    """Postfix evaluator takes a postfix expressions as input and evaluates it."""

    def __init__(self):
        self._error_message = ErrorMessages()
        self._operations = ArithmeticOperations()
        self._values_stack = []

    def evaluate(self, calculation: Calculation) -> Calculation:
        """Get RPN from Calculation class, evaluates it and returns the result back
        to Calculation class.

        Time complexity: O(n).

        Args:
            calculation (Calculation): Object contains the RPN expression to be evaluated.

        Raises:
            ValueError: If there are not enough values in the expression to perform_on
                the arithmetic operation.complete
        """
        # Check that expression exists
        if not calculation.result_rpn:
            raise ExpressionError(self._error_message.get('expression not found'))

        # Split the input expression into symbols using whitespace as a separator
        symbols = calculation.result_rpn.split(' ')

        # Iterate over each symbol in the expression
        for symbol in symbols:
            # If the symbol starts with a numeral, append it to stack
            if symbol[0].isnumeric():
                try:
                    # Convert the symbol to a Decimal and push it into the stack
                    self._values_stack.append(Decimal(symbol))
                except InvalidOperation as exc:
                    raise ExpressionError(self._error_message.get('not a number')) from exc

            # If symbol has a length > 1 and its second character is a numeric,
            # it is a negative value and not a negation (that is an operator)
            elif len(symbol) > 1 and symbol[1].isnumeric():
                try:
                    # Convert the symbol to a Decimal and push it into the stack
                    self._values_stack.append(Decimal(symbol))
                except InvalidOperation as exc:
                    raise ExpressionError(self._error_message.get('not a number')) from exc

            # If the symbol is not a number, then it must be a operator or a function
            else:
                if symbol in self._operations.functions:
                    # If symbol is a function, pop only one value
                    value_2 = None
                    value_1 = self._values_stack.pop()
                elif symbol in self._operations.arithmetic and len(self._values_stack) >= 2:
                    # If symbol is an operator, pop two values
                    value_2 = self._values_stack.pop()
                    value_1 = self._values_stack.pop()
                else:
                    raise ExpressionError(self._error_message.get('not a valid expression'))

                # Perform the operation with the current symbol
                # and two values {None, rational number}
                result = self._operations.perform_on(symbol, value_1, value_2)

                # Push the result into the stack
                self._values_stack.append(result)

        if len(self._values_stack) == 1:
            # The final result is the only value remaining on the stack
            final_result = self._values_stack.pop()
            calculation.result = final_result
        else:
            raise ExpressionError(self._error_message.get('not a valid expression'))
