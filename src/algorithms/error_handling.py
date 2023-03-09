"""Error handling classes."""


class VariableError(Exception):
    """This class handles all the errors concerning variables."""


class ExpressionError(Exception):
    """This class handles all the errors concerning expressions."""


class OperationError(Exception):
    """This class handles all the errors concerning operations."""


class ErrorMessages:
    """This class contains all the error messages."""

    def __init__(self):
        _msg_prefix = 'Err: '

        self.operation_errors = {
            'division by zero': f'{_msg_prefix}Division by zero!',
            'square root':      f'{_msg_prefix}Square root has a value equal or smaller than zero!',
            'logarithm':        f'{_msg_prefix}Logarithm has a value equal or smaller than zero!',
            'missing operand':  f'{_msg_prefix}Invalid or missing operator, function or constant!',
        }

        self.expression_errors = {
            'expression not found': f'{_msg_prefix}Expression not found!',
            'not a valid expression': f'{_msg_prefix}Not a valid expression!',
            'not a number':  f'{_msg_prefix}Not a rational number!',
        }

        self.variable_errors = {
            'no value': f'{_msg_prefix}Variable has no value!',
            'not a number': f'{_msg_prefix}Variable value is not a rational number!',
        }
