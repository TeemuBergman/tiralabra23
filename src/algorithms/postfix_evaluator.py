from decimal import Decimal
from algorithms.basic_operations import basic_operations


def postfix_evaluator(expr):
    """
    Evaluate a postfix expression.

    Args:
        expr (str): The postfix expression to evaluate.

    Returns:
        Decimal: The result of the expression.

    Raises:
        ValueError: If there are not enough values in the expression to perform
            the arithmetic operation.
    """
    # Check if the input expression is empty
    if not expr:
        return None

    # Create a stack to store intermediate results
    stack = []

    # Split the input expression into symbols using whitespace as a separator
    symbols = expr.split()

    # Iterate over each symbol in the expression
    for symbol in symbols:
        # If the symbol starts with a digit, it's a number
        if symbol[0].isnumeric():
            # Convert the symbol to a float and push it onto the stack
            stack.append(Decimal(symbol))

        # If the symbol is NaN, it must be an operator
        else:
            # Try to perform arithmetic operation with symbol and values in
            # stack
            try:
                # Pop the last two values from the stack
                value_2 = stack.pop()
                value_1 = stack.pop()

                # Perform the operation with the symbol and the two values
                result = basic_operations(symbol, value_1, value_2)

                # Push the result onto the stack
                stack.append(result)

            except IndexError as exc:
                # If there are not enough values in the stack, raise an error
                raise ValueError(
                    "Not enough values in the expression") from exc

    # The final result is the only value remaining on the stack
    return stack.pop()
