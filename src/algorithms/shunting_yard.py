from algorithms.error_handling import InputError


class ShuntingYard:
    """
    Shunting yard algortihm converts mathematical expression to a postfix expression.
    """

    def __init__(self):
        self._operator_precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
        self._operator_stack = []
        self._output_stack = []
        self._current_symbol = ''
        self._next_is_number = False
        self._prev_is_number = False
        self._is_negative = False

    def convert(self, calculation) -> str:
        """
        Convert an infix mathematical expression to postfix notation.

        Returns:
            output_queue (str): The postfix expression in string format.
        """

        # List of arithmetic symbols needed for iteration
        symbols = ['+', '-', '*', '/', '^', '(', ')']

        # Check length of the expression
        expression_lenght = len(calculation.expression) - 1

        # Iterate through each character in given expression
        for step, symbol in enumerate(calculation.expression):
            # Update current step and symbol
            self._current_symbol = symbol

            # Check if next symbol is an operator
            if step < expression_lenght:
                self._next_is_number = calculation.expression[step +
                                                              1] not in symbols

            # Process expressions different symbols
            if self._current_symbol == '-':
                self._process_negative()
            elif self._current_symbol.isnumeric():
                self._process_numerals()
            elif self._current_symbol in ('.', ','):
                self._append_to_output_stack()
            elif self._current_symbol in self._operator_precedence:
                self._process_operators()
            elif self._current_symbol in ('(', ')'):
                self._process_parenthesis()

            # Check if current symbol is a number
            self._prev_is_number = self._current_symbol not in symbols

        # Pop any remaining operators from the stack and add them to the output
        while self._operator_stack:
            self._output_stack.append(self._operator_stack.pop())

        # Return the postfix notation as a string
        return ' '.join(self._output_stack)

    def _process_negative(self) -> None:
        # Check if previous symbol is not a number and next one is
        if not self._prev_is_number and self._next_is_number:
            # If true, append negative operator to output_stack
            self._output_stack.append(self._current_symbol)
            # Set state of negative integer flag to True
            self._is_negative = True
        else:
            # If false, add it to operator_stack
            self._operator_stack.append(self._current_symbol)

    def _process_numerals(self) -> None:
        # Check if previous symbol is a number or negative number flag is True
        if self._prev_is_number or self._is_negative:
            # If true, pop output_stack and add it back with current_symbol
            self._output_stack.append(
                self._output_stack.pop() + self._current_symbol)
            # Set negative number flag to False (normal state)
            self._is_negative = False
        else:
            self._output_stack.append(self._current_symbol)

    def _append_to_output_stack(self) -> None:
        # Pop a value from output_stack and append current_symbol to it
        self._output_stack.append(
            self._output_stack.pop() + self._current_symbol)

    def _process_operators(self) -> None:
        """
        Process an operator symbol and update the operator stack and output queue.

        The function uses the `operator_precedence` dictionary to determine the precedence
        level of the input symbol and the operators on the stack.Once the correct position for
        the input symbol is found, it is added to the operator stack.

        Returns:
            None
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

        Returns:
            None
        """

        # If the character is an left parenthesis,
        # push it to the operator stack
        if self._current_symbol == '(':
            self._operator_stack.append(self._current_symbol)
        # If the character is a right parenthesis, pop operators from the stack
        # and add them to the output until an left parenthesis is found
        elif self._current_symbol == ')':
            while self._operator_stack and self._operator_stack[-1] != '(':
                self._output_stack.append(self._operator_stack.pop())
            self._operator_stack.pop()
