class InputError(Exception):
    """
    This class handles all input errors.
    """
    def __init__(self, message):
        self.message = message
        print(message)
