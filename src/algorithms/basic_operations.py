from decimal import Decimal, DivisionByZero, Overflow


def basic_operations(operator, value_1, value_2):
    """
    Perform basic arithmetic operations on two values.

    Args:
        operator (str): The symbol representing the desired operation (+, -, *, /, or ^).
        value_1 (float or str): The first value to be operated on.
        value_2 (float or str): The second value to be operated on.

    Returns:
        float: The result of the operation, as a float.

    Raises:
        ValueError: If the operator is not found, if a division by zero occurs,
            or if an overflow occurs.
    """

    # Convert the values to Decimal objects to ensure decimal precision
    value_1 = Decimal(value_1)
    value_2 = Decimal(value_2)

    # Define a dictionary of operations with the operator symbols as keys
    operations = {
        '+': value_1 + value_2,
        '-': value_1 - value_2,
        '*': value_1 * value_2,
        '/': value_1 / value_2,
        '^': value_1 ** value_2
    }

    # Try to retrieve the result based on the operator symbol
    try:
        return float(operations[operator])
    # If the operator symbol is not found, return a default value of 0 as a
    # Decimal object
    except KeyError:
        return Decimal(0)
    # If a division by zero occurs, raise a ValueError with an error message
    except DivisionByZero as exc:
        raise ValueError("Division by zero") from exc
    # If a division by zero occurs, raise a ValueError with an error message
    except Overflow as exc:
        raise ValueError("Overflow") from exc
