import unittest

from algorithms.calculation import Calculation


class TestShuntingYard(unittest.TestCase):
    """Tests for Calculation class."""

    def test_empty_variables(self):
        """Test if the function returns empty dictionary with a empty string of variables."""
        result = Calculation('', '')
        self.assertEqual(result.variables_dict, {})

    def test_variables_dictionary_1(self):
        """Test if the function returns correct dictionary with a string of variables."""
        result = Calculation('', 'x=1, y=2, z=3')
        self.assertEqual(result.variables_dict, {'x': '1', 'y': '2', 'z': '3'})

    def test_variables_in_expression_1(self):
        """Test if the function returns correct expression with set variables."""
        result = Calculation('x+y+z', 'x=1,y=2,z=3')
        self.assertEqual(result.expression, '1+2+3')

    def test_variables_in_expression_2(self):
        """Test if the function returns correct expression with set variables with spaces."""
        result = Calculation('x+y+z', 'x=1.2, y=2.4, z=3.6')
        self.assertEqual(result.expression, '1.2+2.4+3.6')

    def est_variables_2(self):
        """Test if the function returns correct dictionary with a string of variables."""
        result = Calculation('', 'kg=1.5,meter=2,negative=-3')
        self.assertEqual(result, {'kg': '1.5', 'meter': '2', 'negative': '-3'})
