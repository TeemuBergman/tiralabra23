from decimal import Decimal
from algorithms.basic_operations import basic_operations


class PostfixEvaluator:
    """
    Postfix evaluator takes an postfix expressions as input and evaluates it.
    """

    def __init__(self):
        self.symbols = ''
        self.stack = []

    def evaluate(self, expression) -> Decimal:
        """
        Evaluate a postfix expression.

        Args:
            expression (str): The postfix expression to evaluate.

        Returns:
            Decimal: The result of the expression.

        Raises:
            ValueError: If there are not enough values in the expression to perform
                the arithmetic operation.
        """

        # Check if the input expression is empty
        if not expression:
            return None

        # Split the input expression into symbols using whitespace as a separator
        self.symbols = expression.split()

        # Iterate over each symbol in the expression
        for symbol in self.symbols:
            # If the symbol starts with a digit, it's a number
            if symbol[0].isnumeric():
                # Convert the symbol to a float and push it onto the stack
                self.stack.append(Decimal(symbol))

            # If the symbol is NaN, it must be an operator
            else:
                # Try to perform arithmetic operation with symbol and values in
                # stack
                try:
                    # Pop the last two values from the stack
                    value_2 = self.stack.pop()
                    value_1 = self.stack.pop()

                    # Perform the operation with the symbol and the two values
                    result = basic_operations(symbol, value_1, value_2)

                    # Push the result onto the stack
                    self.stack.append(result)

                except IndexError as exc:
                    # If there are not enough values in the stack, raise an error
                    raise ValueError("Not enough values in the expression") from exc

        # The final result is the only value remaining on the stack
        return self.stack.pop()
