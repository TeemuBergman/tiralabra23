class ShuntingYard:
    """
    Shunting yard algortihm converts mathematical expression to a postfix expression.
    """

    def __init__(self):
        self._expression_lenght = 0
        self._step = 0
        self._temp_queue = ''
        self._operator_stack = []
        self._output_queue = []
        self._next_symbol = None

    def convert(self, calculation) -> str:
        """
        Convert an infix mathematical expression to postfix notation.

        Returns:
            output_queue (str): The postfix expression in string format.
        """

        self._expression_lenght = len(calculation.expression) - 1

        # Iterate through each character in given expression
        for i, symbol in enumerate(calculation.expression):
            # Update current step of iteration
            self._step = i

            if i == self._expression_lenght:
                self._next_symbol = None
            else:
                self._next_symbol = calculation.expression[i + 1]

            # Process numerals and operators

            self._process_numerals(symbol)
            self._process_dots(symbol)
            self._process_operators(symbol)
            self._process_parenthesis(symbol)

        # Pop any remaining operators from the stack and add them to the output
        while self._operator_stack:
            self._output_queue.append(self._operator_stack.pop())

        # Return the postfix notation as a string
        return ' '.join(self._output_queue)

    def _process_numerals(self, symbol) -> None:
        """
        Args:
            symbol (str): The character to be processed.

        Returns:
            None
        """

        # If the character is a digit or a decimal point
        # add it to the temporary queue for grouping symbols
        if symbol.isnumeric():
            self._temp_queue += symbol
            self._process_temp_queue()

        # If there are any symbols in temp queue
        # copy it to output queue and clear temp queue
        elif self._temp_queue:
            self._output_queue.append(self._temp_queue)
            self._temp_queue = ''

    def _process_dots(self, symbol) -> None:
        if symbol == '.':
            self._temp_queue += symbol
            self._process_temp_queue()

    def _process_temp_queue(self) -> None:
        # Check if current symbol is the last on given expression
        if self._step == self._expression_lenght:
            self._output_queue.append(self._temp_queue)

    def _process_operators(self, symbol) -> None:
        """
        Process an operator symbol and update the operator stack and output queue.

        The function uses the `operator_precedence` dictionary to determine the precedence
        level of the input symbol and the operators on the stack.Once the correct position for
        the input symbol is found, it is added to the operator stack.

        Args:
            symbol (str): A string representing an operator symbol.

        Returns:
            None
        """

        # Define precedence levels for operators
        operator_precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
        # If the symbol is an operator, pop operators from the stack
        # and add them to the output until a lower precedence operator is found
        if symbol in operator_precedence:
            while self._operator_stack and operator_precedence.get(
                    symbol) <= operator_precedence.get(self._operator_stack[-1], 0):
                self._output_queue.append(self._operator_stack.pop())
            self._operator_stack.append(symbol)

    def _process_parenthesis(self, symbol) -> None:
        """
        Process a parenthesis symbol in the input expression.

        If the symbol is an open parenthesis, push it onto the operator stack.
        If the symbol is a close parenthesis, pop operators from the stack and
        add them to the output queue until an open parenthesis is found. The
        open parenthesis is also popped from the stack but not added to the output.

        Args:
            symbol (str): A symbol from the input expression.

        Returns:
            None
        """

        # If the character is an left parenthesis,
        # push it to the operator stack
        if symbol == '(':
            self._operator_stack.append(symbol)
        # If the character is a right parenthesis, pop operators from the stack
        # and add them to the output until an left parenthesis is found
        elif symbol == ')':
            while self._operator_stack and self._operator_stack[-1] != '(':
                self._output_queue.append(self._operator_stack.pop())
            self._operator_stack.pop()
