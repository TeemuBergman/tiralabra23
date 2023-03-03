import pathlib
import pygubu

from algorithms.error_handling import InputError
from algorithms.scientific_calculator import ScientificCalculator


# Set GUI constants
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "scical_gui.ui"


class SciCalGui:
    def __init__(self, master=None):
        # Error handler
        input_errors = InputError(self)

        # Create a builder
        self.builder = pygubu.Builder()

        # Load an ui file
        self.builder.add_resource_path(PROJECT_PATH)
        self.builder.add_from_file(PROJECT_UI)

        # Create the widget using a master as parent
        self.mainwindow = self.builder.get_object("main_window", master)

        # Connect callbacks
        self.builder.connect_callbacks(self)

        # Set callbacks to objects
        self.field_output_result = self.builder.get_object('output_result')

        # Set callbacks to variables
        self.string_variable_expression = self.builder.get_variable(
            'string_expression')
        self.string_variable_variables = self.builder.get_variable(
            'string_variables')
        self.string_variable_result = self.builder.get_variable(
            'string_result')
        self.string_variable_result_rpn = self.builder.get_variable(
            'string_result_rpn')

        # Numpad
        # self.numpad_value = builder.tkvariables
        self.input_button_1 = self.builder.get_object('input_button_1')

        # Init variables
        self.expression = ''
        self.variables = ''
        self.result = ''
        self.result_rpn = ''

        # Set focus to expression input
        # self.builder.get_object('input_expression').focus()

    def run(self):
        self.mainwindow.mainloop()

    def display_error_message(self, error_message):
        self.result = 'error'

    def _update_gui(self, symbol):
        self.expression += symbol
        self.string_variable_expression.set(self.expression)

    def call_clear(self, event=None):
        # Clear variables
        self.expression = ''
        self.variables = ''
        self.result = ''
        self.result_rpn = ''

        # Send empty values to GUI
        self.string_variable_expression.set(self.expression)
        self.string_variable_variables.set(self.variables)
        self.string_variable_result.set(self.result)
        self.string_variable_result_rpn.set(self.result_rpn)

    def call_calculate(self, event=None):
        # Create new calculator
        calculator = ScientificCalculator()

        # Get variables 'expression' and 'variables' from GUI
        self.expression = self.string_variable_expression.get()
        self.variables = self.string_variable_variables.get()

        # Calculate
        result = calculator.calculate(self.expression, self.variables)

        # Convert to string
        result = self._convert_to_str(result)

        self.string_variable_result_rpn.set(calculator.result_rpn)

        # Set result to GUI
        self.string_variable_result.set(result)

    def _convert_to_str(self, value) -> str:
        """Convert given value to a string and modify if it ends at .0"""

        cleaned = str(value)

        # If input value is a decimal with .0 at the end
        if cleaned.endswith('.0'):
            # remove '.0' from end of string
            return cleaned[:-2]

        return cleaned

    def call_numpad(self, widget_id):
        """
        This is not the optimal solution for handling button inputs,
        but it's the only one Pygubu offers at the moment.
        I will rewrite this if I find a better sollution.
        """
        match widget_id:
            case 'input_button_1':
                self._update_gui('1')
            case 'input_button_2':
                self._update_gui('2')
            case 'input_button_3':
                self._update_gui('3')
            case 'input_button_4':
                self._update_gui('4')
            case 'input_button_5':
                self._update_gui('5')
            case 'input_button_6':
                self._update_gui('6')
            case 'input_button_7':
                self._update_gui('7')
            case 'input_button_8':
                self._update_gui('8')
            case 'input_button_9':
                self._update_gui('9')
            case 'input_button_0':
                self._update_gui('0')
            case 'input_button_dot':
                self._update_gui('.')
            case 'input_button_add':
                self._update_gui('+')
            case 'input_button_subtract':
                self._update_gui('-')
            case 'input_button_divide':
                self._update_gui('/')
            case 'input_button_multiply':
                self._update_gui('*')
            case 'input_button_left_parentheses':
                self._update_gui('(')
            case 'input_button_right_parentheses':
                self._update_gui(')')
            case 'input_button_exponent':
                self._update_gui('^')
            case 'input_button_square_root':
                self._update_gui('sqr(x)')


if __name__ == "__main__":
    app = SciCalGui()
    app.run()
