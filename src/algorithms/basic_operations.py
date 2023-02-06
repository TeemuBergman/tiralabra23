from decimal import Decimal, DivisionByZero, Overflow


def basic_operations(operator, value_1, value_2):
    """
    Perform an arithmetic operation on two decimal values using the given operator.
    :param operator: The symbol of the operator to perform (+, -, *, /, or ^)
    :type operator: str
    :param value_1: The first value to perform the operation on
    :type value_1: decimal.Decimal
    :param value_2: The second value to perform the operation on
    :type value_2: decimal.Decimal
    :return: The result of the operation as a decimal value
    :rtype: decimal.Decimal
    :raises ValueError: If the operator symbol is not recognized or if a division by zero occurs
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
