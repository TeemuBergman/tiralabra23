def shunting_yard(expr, var=None):
    """
    Convert an infix mathematical expression to postfix notation.

    Parameters:
        expr (str): The infix mathematical expression to be converted to postfix notation.
        var (dict): Dictionary of variables used in expresssion.

    Returns:
        output_queue (str): The postfix expression in string format.
    """

    # Check if the input expression is empty
    if not expr:
        return None

    # Replace variables in `expr` with values from `var` if `var` is True
    if var:
        expr = introduce_variables(expr, var)

    # Create stacks for operators and output
    operator_stack = []
    output_queue = []
    # Define precedence levels for operators
    operator_precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    # Create temp queue and calculate expression lenght used in iteration
    temp_queue = ''
    expr_lenght = len(expr) - 1

    # Iterate through each character in given expression
    for i, symbol in enumerate(expr):
        # If the character is a digit or a decimal point
        # add it to the temporary queue for grouping symbols
        if symbol.isnumeric() or symbol == '.':
            temp_queue += symbol
            # Check if current symbol is the last on given expression
            if i == expr_lenght:
                output_queue.append(temp_queue)
        # If there are any symbols in temp queue
        # copy it to output queue and clear temp queue
        elif temp_queue:
            output_queue.append(temp_queue)
            temp_queue = ''

        # If the symbol is an operator, pop operators from the stack
        # and add them to the output until a lower precedence operator is found
        if symbol in operator_precedence:
            while operator_stack and operator_precedence.get(
                    symbol) <= operator_precedence.get(operator_stack[-1], 0):
                output_queue.append(operator_stack.pop())
            operator_stack.append(symbol)
        # If the character is an open parenthesis, push it to the operator
        # stack
        elif symbol == '(':
            operator_stack.append(symbol)
        # If the character is a close parenthesis, pop operators from the stack
        # and add them to the output until an open parenthesis is found
        elif symbol == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()

    # Pop any remaining operators from the stack and add them to the output
    while operator_stack:
        output_queue.append(operator_stack.pop())

    # Return the postfix notation as a string
    return ' '.join(output_queue)


def introduce_variables(expression, variables):
    """
    Replace variables in an expression with values from a dictionary.

    Args:
        expression (str): The expression to replace variables in.
        variables (dict): A dictionary of variable names (as keys) and values.

    Returns:
        str: The expression with variables substituted by values from the dictionary.
    """

    for key, value in variables.items():
        expression = expression.replace(key, value)
    return expression
