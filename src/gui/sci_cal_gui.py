"""Scientific Calculator Graphical User Interface class."""

import sys
import pathlib
import pygubu

# Custom classes
from calculator.scientific_calculator import ScientificCalculator
from .gui_functions import GUIFunctions
from .memory import Memory

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
        self.entry_input_expression = self.builder.get_object('input_expression')

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
        self.result = 0
        self.result_rpn = ''
        self.history = []

        # Calculators memory functionality
        self.memory = Memory()

        # Set focus to expression input
        self.builder.get_object('input_expression').focus()

    def run(self):
        self.main_window.mainloop()

    def _update_expression_entry(self, symbol):
        input_expression = self.input_expression.get()
        symbol = str(symbol)
        self.expression = input_expression + symbol

        # Set updated expression to GUI
        self.input_expression.set(self.expression)
        # Move cursor to the end of expression
        self.entry_input_expression.icursor(len(self.expression))

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

    def call_calculate(self, event=None):
        """Execute the given expression and print its output to GUIs output fields."""
        # Create new calculator
        self.calculator = ScientificCalculator()

        # Get variables 'expression' and 'variables' from GUI
        self.expression = self.input_expression.get()
        self.variables = self.input_variables.get()

        try:
            # Calculate
            self.result = self.calculator.calculate(self.expression, self.variables)
            # Set results to GUI
            self.output_result.set(self.result)
            self.output_result_rpn.set(self.calculator.calculation.result_rpn)
            # Update history panel
            self.update_history(self.calculator.calculation)
        except:
            self._display_error()

    def _display_error(self):
        # Set error message and clear RPN result
        self.output_result.set(sys.exc_info()[1])
        self.output_result_rpn.set('')

    def update_history(self, calculation) -> None:
        if len(self.history) >= 18:
            self.history = self.history[2:]
            self.history.append(f'{calculation.expression}=')
            self.history.append(calculation.result)
        else:
            self.history.append(f'{calculation.expression}=')
            self.history.append(calculation.result)

        self.output_history.set(self.history)

    def call_numpad(self, widget_id):
        """Handles all the corresponding button presses from GUI."""
        self._update_expression_entry(self.gui_functions.buttons[widget_id])

    def call_memory(self, command) -> None:
        """Calculators result saving and recalling functionality."""
        # Get last result or init to 0
        if self.result:
            result = self.result
        else:
            result = 0

        match command:
            case 'button_m_save':
                self.memory.save_to_memory(result)
            case 'button_m_add':
                self.memory.add_to_memory(result)
            case 'button_m_subtract':
                self.memory.subtract_from_memory(result)
            case 'button_m_read':
                # self.input_expression.set(str(self.memory.saved_value))
                self._update_expression_entry(self.memory.saved_value)
            case 'button_m_clear':
                self.memory.clear_memory()
