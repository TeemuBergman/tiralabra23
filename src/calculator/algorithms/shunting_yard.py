"""Shunting Yard class."""

from collections import deque

# Custom classes
from utils.error_handling import ErrorMessages, ExpressionError
from .calculation import Calculation


class ShuntingYard:
    """
    Shunting yard algorithm converts mathematical expression to a postfix expression.
    """

    def __init__(self):
        self._error_message = ErrorMessages()
        self._operator_stack = []
        self._output_stack = []
        self._current_symbol = ''
        self._history = deque(' ')
        self._decimal_value = False
        self._operator_stack_has_function = False

    def convert(self, calculation: Calculation) -> None:
        """
        Converts an infix mathematical expression to a Reverse Polish Notation (RPN).

        Args:
            calculation (Calculation): Takes the Calculation class as argument and saves
            the result to it as Reverse Polish Notation.
        """
        # Check length of the expression
        expression_length = len(calculation.expression) - 1

        # Iterate through each character in given expression
        for step, symbol in enumerate(calculation.expression):
            # Update current step and symbol
            self._current_symbol = symbol

            # Check if next symbol is a number
            if step < expression_length:
                self._history.append(calculation.expression[step + 1])

            # Process expressions different symbols
            if self._current_symbol.isnumeric():
                self._process_values()
            elif self._current_symbol == '.':
                self._process_decimals()
            elif self._current_symbol == '-':
                self._process_negatives()
            elif self._current_symbol in ['+', '*', '/', '^']:
                self._process_operators()
            elif self._current_symbol in ('(', ')'):
                self._process_parenthesis()
            else:  # If it's not any above, then it must be a function
                self._process_functions()

            # Save current symbol as previous
            self._history.appendleft(symbol)

        # Pop any remaining operators from the stack and add them to the output
        self._remaining_operators()

        # Save the result to Calculation
        calculation.result_rpn = ' '.join(self._output_stack)

    def _process_functions(self) -> None:
        """Handles all the functions to operator stack in correct composition."""
        if self._operator_stack and self._operator_stack_has_function and self._operator_stack[-1] != '(':
            self._operator_stack.append(self._operator_stack.pop() + self._current_symbol)
        else:
            self._operator_stack.append(self._current_symbol)
            self._operator_stack_has_function = True

    def _process_negatives(self) -> None:
        """Handles all the negative values and parentheses.

        Check for different cases where negative operator is used without its
        counterpart value and if some our found add 0 to output stack.
        """

        # Cases: -(, (-(
        if self._history[0] in [' ', '('] and self._history[-1] == '(':
            self._output_stack.append('0')
        # Cases: -n, (-n
        elif self._history[0] in [' ', '('] and self._history[-1].isnumeric():
            self._output_stack.append('0')
        # Process negative operator as normal
        self._process_operators()

    def _process_decimals(self) -> None:
        """Handles dots in decimal values."""
        if self._history[0].isnumeric():
            self._output_stack.append(self._output_stack.pop() + self._current_symbol)
        self._decimal_value = True

    def _process_values(self) -> None:
        """Handles all values."""
        # Check if previous symbol is a number or the negative value state is True
        if self._history[0].isnumeric() or self._decimal_value:
            # If true, pop output_stack and add it back with current_symbol
            try:
                self._output_stack.append(self._output_stack.pop() + self._current_symbol)
            except IndexError as exc:
                raise ExpressionError(self._error_message.get('not a valid expression')) from exc
            self._decimal_value = False
        else:
            self._output_stack.append(self._current_symbol)

    def _update_last_value_on_output_stack(self) -> None:
        """Pop a value from output_stack and add current_symbol to it and then append it back."""
        self._output_stack.append(self._output_stack.pop() + self._current_symbol)

    def _process_operators(self) -> None:
        """
        Process an operator symbol and update the operator stack and output queue.

        The function uses the `operator_precedence` dictionary to determine the precedence
        level of the input symbol and the operators on the stack.Once the correct position for
        the input symbol is found, it is added to the operator stack.
        """
        # Operator precedence to be used when arranging operators in stack
        operator_precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
        # If the symbol is an operator, pop operators from the stack
        # and add them to the output until a lower precedence operator is found
        while self._operator_stack and operator_precedence.get(
                self._current_symbol) <= operator_precedence.get(
                    self._operator_stack[-1], 0):
            self._output_stack.append(self._operator_stack.pop())
        self._operator_stack.append(self._current_symbol)

    def _process_parenthesis(self) -> None:
        """
        Process a parenthesis symbol in the input expression.

        If the symbol is an open parenthesis, push it onto the operator stack.
        If the symbol is a close parenthesis, pop operators from the stack and
        add them to the output queue until an open parenthesis is found. The
        open parenthesis is also popped from the stack but not added to the output.
        """
        # If the symbol is a left parenthesis, push it to the operator stack
        if self._current_symbol == '(':
            self._operator_stack.append(self._current_symbol)
        # If the symbol is a right parenthesis, pop operators from the stack
        # and add them to the output stack until a left parenthesis is found
        else:
            while self._operator_stack:
                if self._operator_stack[-1] != '(':
                    self._output_stack.append(self._operator_stack.pop())
                elif self._operator_stack_has_function:
                    # There is a function after left parentheses
                    self._operator_stack.pop()
                    self._output_stack.append(self._operator_stack.pop())
                    self._operator_stack_has_function = False
                else:
                    # Pop the left parentheses
                    self._operator_stack.pop()
                    break

    def _remaining_operators(self) -> None:
        """
        Pop any remaining operators from the stack and add them to the output
        and raise an ExpressionError if left parentheses has been found.
        """
        while self._operator_stack:
            if self._operator_stack[-1] != '(':
                self._output_stack.append(self._operator_stack.pop())
            else:
                raise ExpressionError(self._error_message.get('not a valid expression'))
