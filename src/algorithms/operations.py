import math
from decimal import Decimal, DivisionByZero, Overflow, InvalidOperation


class Operations:
    """This class handles all arithmetic operations."""

    def __init__(self):
        self.result = None

    def perform_on(self, operator: str, value_1: float, value_2 = None) -> Decimal:
        """
        Perform basic arithmetic operations on two values.

        Args:
            operator (str): The symbol representing the desired operation (+, -, *, /, or ^).
            value_1 (float): The first value to be operated on.
            value_2 (float): The second value to be operated on.

        Returns:
            float: The result of the operation, as a float.

        Raises:
            ValueError: If the operator is not found, if a division by zero occurs,
                or if an overflow occurs.
        """

        # Check that there is an operator
        if not operator:
            raise ValueError("Operator missing!")

        # Convert the values to Decimal objects to ensure decimal precision
        value_1 = Decimal(value_1)
        if value_2:
            value_2 = Decimal(value_2)

        # Perform arithmetics
        if operator == '+':
            self.result = value_1 + value_2
        elif operator == '-':
            self.result = value_1 - value_2
        elif operator == '*':
            self.result = value_1 * value_2
        elif operator == '/':
            # If a division by zero occurs, raise a ValueError with an error message
            try:
                self.result = value_1 / value_2
            except DivisionByZero:
                raise ValueError("Division by zero!")
        elif operator == '^':
            self.result = value_1 ** value_2
        elif operator == 'sin':
            self.result = Decimal(math.sin(value_1))
        elif operator == 'cos':
            self.result = Decimal(math.cos(value_1))
        elif operator == 'tan':
            self.result = Decimal(math.tan(value_1))
        else:
            raise ValueError("Invalid operator!")

        # Return the operation result
        return self.result
