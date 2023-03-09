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
        self._msg_prefix = 'Err: '
        self._msg_postfix = '!'

        self._operation_errors = {
            'division by zero': 'Division by zero',
            'square root':      'Square root has a value equal or smaller than zero',
            'logarithm':        'Logarithm has a value equal or smaller than zero',
            'random':           'Random has a value equal or smaller than zero',
            'use integer':      'Use a integer value',
            'missing operand':  'Invalid or missing operator, function or constant',
            'missing value':    'Invalid or missing value'
        }

        self._expression_errors = {
            'expression not found': 'Expression not found',
            'not a valid expression': 'Not a valid expression',
            'not a number':  'Not a rational number'
        }

        self._variable_errors = {
            'no value': 'Variable has no value',
            'not a variable': 'Variable value is not a rational number'
        }

    def get(self, error: str) -> str:
        """Finds a correct error message and adds a prefix and postfix to it."""
        if error in self._operation_errors:
            error_message = self._operation_errors[error]
        elif error in self._expression_errors:
            error_message = self._expression_errors[error]
        elif error in self._variable_errors:
            error_message = self._variable_errors[error]
        else:
            return 'Error message not found!'

        return f'{self._msg_prefix}{error_message}{self._msg_postfix}'
