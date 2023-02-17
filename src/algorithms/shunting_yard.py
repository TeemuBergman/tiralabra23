class ShuntingYard:
    """
    Lorem
    """

    def __init__(self):
        self._expression_lenght = 0
        self._step = 0
        self._temp_queue = ''
        self._operator_stack = []
        self._output_queue = []

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
            # If the character is a digit or a decimal point
            # add it to the temporary queue for grouping symbols
            self._process_numerals(symbol)
            self._process_operators(symbol)

        # Pop any remaining operators from the stack and add them to the output
        while self._operator_stack:
            self._output_queue.append(self._operator_stack.pop())

        # Return the postfix notation as a string
        return ' '.join(self._output_queue)

    def _process_numerals(self, symbol):
        if symbol.isnumeric() or symbol == '.':
            self._temp_queue += symbol
            # Check if current symbol is the last on given expression
            if self._step == self._expression_lenght:
                self._output_queue.append(self._temp_queue)
            # If there are any symbols in temp queue
            # copy it to output queue and clear temp queue
        elif self._temp_queue:
            self._output_queue.append(self._temp_queue)
            self._temp_queue = ''

    def _process_operators(self, symbol):
        # Define precedence levels for operators
        operator_precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

        # If the symbol is an operator, pop operators from the stack
        # and add them to the output until a lower precedence operator is found
        if symbol in operator_precedence:
            while self._operator_stack and operator_precedence.get(
                    symbol) <= operator_precedence.get(self._operator_stack[-1], 0):
                self._output_queue.append(self._operator_stack.pop())
            self._operator_stack.append(symbol)
        # If the character is an open parenthesis, push it to the operator
        # stack
        elif symbol == '(':
            self._operator_stack.append(symbol)
        # If the character is a close parenthesis, pop operators from the stack
        # and add them to the output until an open parenthesis is found
        elif symbol == ')':
            while self._operator_stack and self._operator_stack[-1] != '(':
                self._output_queue.append(self._operator_stack.pop())
            self._operator_stack.pop()
