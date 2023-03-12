"""Shunting Yard class."""

from collections import deque

# Custom classes
from utils.error_handling import ErrorMessages, ExpressionError
from .calculation import Calculation


class ShuntingYard:  # pylint: disable=too-few-public-methods
    """Shunting yard algorithm converts mathematical expression to a postfix expression."""

    def __init__(self):
        self._error_message = ErrorMessages()
        self._operands = []
        self._output_rpn = []
        self._current_symbol = ''
        self._symbol_oracle = deque(' ')  # Knows its history and sees into the future

    def convert(self, calculation: Calculation) -> None:
        """Converts an infix mathematical expression to a Reverse Polish Notation (RPN).

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
                self._symbol_oracle.append(calculation.expression[step + 1])

            # Process expressions different symbols
            if self._current_symbol.isnumeric():
                self._process_integers()
            elif self._current_symbol == '.':
                self._process_decimals()
            elif self._current_symbol == '-':
                self._process_negatives()
            elif self._current_symbol in ['+', '*', '/', '^', '%']:
                self._process_operators()
            elif self._current_symbol in ['(', ')']:
                self._process_parenthesis()
            elif self._current_symbol.isalpha():
                self._process_functions()
            else:
                raise ExpressionError(self._error_message.get('not a valid expression'))

            # Save current symbol as previous
            self._symbol_oracle.appendleft(symbol)

        # Pop any remaining operators from the stack and add them to the output
        self._remaining_operators()

        # Save the result to Calculation
        calculation.result_rpn = ' '.join(self._output_rpn)

    def _process_integers(self) -> None:
        """Handles all integers.

        Check if current_symbol is integer and if it is a part of rational number.
        """
        # {'.n'}
        if self._symbol_oracle[0] == '.':
            self._output_rpn.append(self._output_rpn.pop() + self._current_symbol)
        # {'nn'}
        elif self._symbol_oracle[0].isnumeric():
            self._output_rpn.append(self._output_rpn.pop() + self._current_symbol)
        # {' '}
        else:
            self._output_rpn.append(self._current_symbol)

    def _process_decimals(self):
        """Handles the dot in rational numbers.

        Check if previous symbol is integer or if it just a dot,
        then add 0 as the first value.
        """
        # {'n.'}
        if self._symbol_oracle[0].isnumeric():
            self._output_rpn.append(self._output_rpn.pop() + self._current_symbol)
        # {'.n}'
        else:
            self._output_rpn.append('0' + self._current_symbol)

    def _process_negatives(self) -> None:
        """Handles all the negative values and parentheses.

        Check for different cases where negative operator is used without its
        counterpart value and if some our found add 0 to output stack.
        """
        # {'-(', '(-('}
        if self._symbol_oracle[0] in [' ', '('] and self._symbol_oracle[-1] == '(':
            self._output_rpn.append('0')
        # {'-n', '(-n'}
        elif self._symbol_oracle[0] in [' ', '('] and self._symbol_oracle[-1].isnumeric():
            self._output_rpn.append('0')
        # {'-function'}
        elif self._symbol_oracle[-1].isalpha():
            self._output_rpn.append('0')

        # Process negative operator just like any other of its kind
        self._process_operators()

    def _process_functions(self) -> None:
        """Handles all the functions to operator stack in correct composition."""
        # {' '}
        if not self._symbol_oracle[0].isalpha():
            self._operands.append(self._current_symbol)
        # {'cc'}
        else:
            self._operands.append(self._operands.pop() + self._current_symbol)

    def _process_operators(self) -> None:
        """Process an operator symbol and update the operator stack and output queue.

        The function uses the `operator_precedence` dictionary to determine the precedence
        level of the input symbol and the operators on the stack.Once the correct position for
        the input symbol is found, it is added to the operator stack.
        """
        # Operator precedence to be used when arranging operators in stack
        operator_precedence = {'%': 3, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

        # If the symbol is an operator, pop operators from the stack and
        # add them to the output until a lower precedence operator is found
        while self._operands:
            if operator_precedence.get(self._current_symbol) <= \
                    operator_precedence.get(self._operands[-1], 0):
                self._output_rpn.append(self._operands.pop())
            else:
                break

        self._operands.append(self._current_symbol)

    def _process_parenthesis(self) -> None:
        """Process a parenthesis symbol in the input expression.

        If the symbol is an open parenthesis, push it onto the operator stack.
        If the symbol is a close parenthesis, pop operators from the stack and
        add them to the output queue until an open parenthesis is found. The
        open parenthesis is also popped from the stack but not added to the output.
        """
        # If the symbol is a left parenthesis, push it to the operator stack
        if self._current_symbol == '(':
            # If last character was not part of function, append to operator stack
            if not self._symbol_oracle[0].isalpha():
                self._operands.append(self._current_symbol)

        # If the symbol is a right parenthesis, pop operators from the stack
        # and add them to the output stack until a left parenthesis is found
        else:
            while self._operands:
                if self._operands[-1] != '(':
                    self._output_rpn.append(self._operands.pop())
                else:
                    # Pop the left parentheses
                    self._operands.pop()
                    break

    def _remaining_operators(self) -> None:
        """
        Pop any remaining operators from the stack and add them to the output
        and raise an ExpressionError if left parentheses is found.
        """
        while self._operands:
            if self._operands[-1] != '(':
                self._output_rpn.append(self._operands.pop())
            else:
                raise ExpressionError(self._error_message.get('not a valid expression'))
