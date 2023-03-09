"""Shunting Yard class."""

# Custom classes
from utils.error_handling import ErrorMessages, ExpressionError
from .calculation import Calculation


class ShuntingYard:
    """
    Shunting yard algorithm converts mathematical expression to a postfix expression.
    """

    def __init__(self):
        self._error_message = ErrorMessages()
        self._operator_precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
        self._operator_stack = []
        self._output_stack = []
        self._current_symbol = ''
        self._previous_symbol = ''
        self._next_symbol = ''
        self._negative_value = False
        self._decimal_value = False
        self.operator_stack_has_function = False

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
                self._next_symbol = calculation.expression[step + 1]

            # Process expressions different symbols
            if self._current_symbol == '-':
                self._process_negative_values()
            elif self._current_symbol.isnumeric():
                self._process_values()
            elif self._current_symbol == '.':
                self._process_decimals()
            elif self._current_symbol in self._operator_precedence:
                self._process_operators()
            elif self._current_symbol in ('(', ')'):
                self._process_parenthesis()
            else:  # If it's not any above, then it must be a function
                self._process_functions()

            # Save current symbol as previous
            self._previous_symbol = symbol

        # Pop any remaining operators from the stack and add them to the output
        self._remaining_operators()

        # Save the result to Calculation
        calculation.result_rpn = ' '.join(self._output_stack)

    def _process_functions(self) -> None:
        """Handles all the function names to operator stack in correct composition."""
        if self._operator_stack and self.operator_stack_has_function and self._operator_stack[-1] not in '(':
            self._operator_stack.append(self._operator_stack.pop() + self._current_symbol)
        else:
            self._operator_stack.append(self._current_symbol)
            self.operator_stack_has_function = True

    def _process_negative_values(self) -> None:
        """Handles all the negative values."""
        # Check that the previous symbol is not ')' or number and the next one is a number
        if not self._previous_symbol == ')' and not self._previous_symbol.isnumeric() and self._next_symbol.isnumeric():
            # If true, append negative operator to output_stack
            self._output_stack.append(self._current_symbol)
            # Set state of negative integer flag to True
            self._negative_value = True
        else:  # If false, process it as a regular operator
            self._process_operators()

    def _process_decimals(self) -> None:
        """Handles dots in decimal values."""
        if  self._previous_symbol.isnumeric():
            self._output_stack.append(self._output_stack.pop() + self._current_symbol)
        self._decimal_value = True

    def _process_values(self) -> None:
        """Handles all values."""
        # Check if previous symbol is a number or the negative value state is True
        if self._previous_symbol.isnumeric() or self._negative_value or self._decimal_value:
            # If true, pop output_stack and add it back with current_symbol
            try:
                self._output_stack.append(self._output_stack.pop() + self._current_symbol)
            except IndexError as exc:
                raise ExpressionError(self._error_message.get('not a valid expression')) from exc
            # Set the negative and decimal value states to False (normal state)
            self._negative_value = False
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
        # If the symbol is an operator, pop operators from the stack
        # and add them to the output until a lower precedence operator is found
        while self._operator_stack and self._operator_precedence.get(
                self._current_symbol) <= self._operator_precedence.get(
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
        if self._current_symbol in '(':
            # Check if the negative operator is the first in expression
            if self._operator_stack and not self._output_stack and self._operator_stack[-1] in '-':
                self._operator_stack.append(self._operator_stack.pop() + self._current_symbol)
            else:
                self._operator_stack.append(self._current_symbol)
        # If the symbol is a right parenthesis, pop operators from the stack
        # and add them to the output stack until a left parenthesis is found
        else:
            while self._operator_stack:
                if self._operator_stack[-1] != '(':
                    self._output_stack.append(self._operator_stack.pop())
                elif self.operator_stack_has_function:
                    # There is a function after left parentheses
                    self._operator_stack.pop()
                    self._output_stack.append(self._operator_stack.pop())
                    self.operator_stack_has_function = False
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
