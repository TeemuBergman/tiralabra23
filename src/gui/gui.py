import pathlib
import pygubu
from algorithms.scientific_calculator import ScientificCalculator


PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "scical_gui.ui"


class ScicalGui:
    def __init__(self, master=None):
        # Tkinter init
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)

        # Main widget
        self.mainwindow = builder.get_object("main_window", master)
        builder.connect_callbacks(self)

        # Set references
        self.field_input_expression = builder.get_object('input_expression')
        self.field_input_variables = builder.get_object('input_variables')
        self.field_output_result = builder.get_object('output_result')
        self.string_variable_result = builder.get_variable('string_result')

        # Set focus to expression input
        self.field_input_expression.focus()

    def run(self):
        self.mainwindow.mainloop()

    def call_calculate(self, event=None):
        calculator = ScientificCalculator()
        expression = self.field_input_expression.get()
        variables = self.field_input_variables.get()
        result = calculator.calculate(expression, variables)
        self.string_variable_result.set(result)


if __name__ == "__main__":
    app = ScicalGui()
    app.run()
