"""Scientific Calculator Graphical User Interface class."""

import sys
import pathlib
import pygubu

# Custom classes
from calculator.scientific_calculator import ScientificCalculator
from .gui_functions import GUIFunctions

# Set GUI constants
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "scical_gui.ui"


class SciCalGui:
    def __init__(self, master=None):
        # Create a GUI builder
        self.builder = pygubu.Builder()

        # Load an ui file
        self.builder.add_resource_path(PROJECT_PATH)
        self.builder.add_from_file(PROJECT_UI)

        # Create the widget using a master as parent
        self.main_window = self.builder.get_object("main_window", master)

        # For controlling button presses
        self.gui_functions = GUIFunctions()

        # Connect callbacks
        self.builder.connect_callbacks(self)

        # Set callbacks to objects
        self.field_output_result = self.builder.get_object('output_result')

        # Set callbacks to variables
        self.input_expression = self.builder.get_variable(
            'string_expression')
        self.input_variables = self.builder.get_variable(
            'string_variables')
        self.output_result = self.builder.get_variable(
            'string_result')
        self.output_result_rpn = self.builder.get_variable(
            'string_result_rpn')
        self.output_history = self.builder.get_variable('list_history')

        # Init variables
        self.expression = ''
        self.variables = ''
        self.result = ''
        self.result_rpn = ''
        self.history = []

        # Set focus to expression input
        self.builder.get_object('input_expression').focus()

    def run(self):
        self.main_window.mainloop()

    def _update_gui(self, symbol):
        self.expression += symbol
        self.input_expression.set(self.expression)

    def call_clear(self, event=None):
        """Clear GUIs input and output fields."""
        # Clear variables
        self.expression = ''
        self.variables = ''
        self.result = ''
        self.result_rpn = ''
        # Send empty values to GUI
        self.input_expression.set(self.expression)
        self.input_variables.set(self.variables)
        self.output_result.set(self.result)
        self.output_result_rpn.set(self.result_rpn)

    def update_history(self, calculation) -> None:
        if len(self.history) >= 18:
            self.history = self.history[2:]
            self.history.append(f'{calculation.expression}=')
            self.history.append(calculation.result)
        else:
            self.history.append(f'{calculation.expression}=')
            self.history.append(calculation.result)
        self.output_history.set(self.history)

    def call_calculate(self, event=None):
        """Execute the given expression and print its output to GUIs output fields."""
        # Create new calculator
        calculator = ScientificCalculator()
        # Get variables 'expression' and 'variables' from GUI
        self.expression = self.input_expression.get()
        self.variables = self.input_variables.get()

        try:
            # Calculate
            self.result = calculator.calculate(self.expression, self.variables)
            # Set results to GUI
            self.output_result.set(self.result)
            self.output_result_rpn.set(calculator.calculation.result_rpn)
            # Update history panel
            self.update_history(calculator.calculation)
        except:
            # Set error message and clear RPN result
            self.output_result.set(sys.exc_info()[1])
            self.output_result_rpn.set('')

    def call_memory(self):
        # TODO - Complete this.
        ...

    def call_numpad(self, widget_id):
        """Handles all the corresponding button presses from GUI."""
        self._update_gui(self.gui_functions.buttons[widget_id])


if __name__ == "__main__":
    app = SciCalGui()
    app.run()
