"""Scientific Calculator GUI Memory functionality."""


class Memory:

    def __init__(self):
        self.saved_value = ''

    def save_to_memory(self, result) -> None:
        """..."""
        self.saved_value = result

    def add_to_memory(self, result) -> None:
        """..."""
        self.saved_value += result

    def subtract_from_memory(self, result) -> None:
        """..."""
        self.saved_value -= result

    def clear_memory(self) -> None:
        """..."""
        self.saved_value = ''
