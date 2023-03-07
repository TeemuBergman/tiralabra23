"""GUI Functions class"""


class GUIFunctions:
    """
    This class handles all the button presses to set a corresponding string to GUI.
    """

    def __init__(self):
        self.buttons = {
            'input_button_0':                 '0',
            'input_button_1':                 '1',
            'input_button_2':                 '2',
            'input_button_3':                 '3',
            'input_button_4':                 '4',
            'input_button_5':                 '5',
            'input_button_6':                 '6',
            'input_button_7':                 '7',
            'input_button_8':                 '8',
            'input_button_9':                 '9',
            'input_button_x':                 'x',
            'input_button_y':                 'y',
            'input_button_z':                 'z',
            'input_button_dot':               '.',
            'input_button_add':               '+',
            'input_button_subtract':          '-',
            'input_button_divide':            '/',
            'input_button_multiply':          '*',
            'input_button_left_parentheses':  '(',
            'input_button_right_parentheses': ')',
            'input_button_exponent':          '^',
            'input_button_sinr':              'sinr(x)',
            'input_button_cosr':              'cosr(x)',
            'input_button_tanr':              'tanr(x)',
            'input_button_sind':              'sind(x)',
            'input_button_cosd':              'cosd(x)',
            'input_button_tand':              'tand(x)',
            'input_button_square_root':       'sqrt(x)',
            'input_button_log':               'log(x)',
            'input_button_demo_1':            '((kissa) * (koira))',
            'input_button_demo_2':            '(sind(x) * x)',
            'input_button_demo_3':            '(x * y + (2 * x ^ (x - (z / 0.5))))',
            'input_button_demo_4':            '((((((((((1))))))) + (((((((1))))))))))'
        }
