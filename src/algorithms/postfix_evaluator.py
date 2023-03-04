"""Postfix Evaluator class."""

from decimal import Decimal

# Custom classes
from algorithms.error_handling import ExpressionError
from algorithms.arithmetic_operations import ArithmeticOperations


class PostfixEvaluator:
    """
    Postfix evaluator takes an postfix expressions as input and evaluates it.
    """

    def __init__(self):
        self.operations = ArithmeticOperations()
        self.symbols = []
        self.stack = []
        self.result = Decimal()
        self.value_1 = Decimal()
        self.value_2 = Decimal()

    def evaluate(self, expression) -> Decimal:
        """
        Evaluate a postfix expression.

        Args:
            expression (str): The postfix expression to evaluate.

        Returns:
            Decimal: The result of the expression.

        Raises:
            ValueError: If there are not enough values in the expression to perform_on
                the arithmetic operation.
        """
        # Check if the input expression is empty
        if not expression:
            raise ExpressionError("Expression not found!")

        # Split the input expression into symbols using whitespace as a separator
        self.symbols = expression.split(' ')

        # Iterate over each symbol in the expression
        for step, symbol in enumerate(self.symbols):
            # Is it safe to probe in to the future
            probing_distance = (step + 1) <= len(symbol)

            # If symbol is a negative sign, then probe if next one is a numeral
            if symbol[0] == '-' and probing_distance:
                self.stack.append(Decimal(symbol))

            # If the symbol starts with a digit or a minus symbol it's a number
            elif symbol[0].isnumeric():

                # Convert the symbol to a Decimal and push it into the stack
                self.stack.append(Decimal(symbol))

            # If the symbol is NaN, then it must be an operator
            else:
                if len(self.stack) >= 2:
                    # Pop the last two values from the stack
                    self.value_2 = self.stack.pop()
                    self.value_1 = self.stack.pop()
                elif len(self.stack) == 1:
                    # If operator is a function
                    self.value_1 = self.stack.pop()
                else:
                    raise ExpressionError('Not a complete expression!')

                # Perform the operation with the symbol and the two values
                result = self.operations.perform_on(symbol, self.value_1, self.value_2)

                # Push the result onto the stack
                self.stack.append(result)

        # The final result is the only value remaining on the stack
        self.result = self.stack.pop()

        return self.result
