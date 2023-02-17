import unittest
from algorithms.calculation import Calculation


class TestShuntingYard(unittest.TestCase):
    """Tests for Calculation class."""

    def test_with_empty_variables(self):
        """Test if the function returns empty dictionary with a empty string of variables."""
        result = Calculation('', '')
        self.assertEqual(result.variables_dict, {})

    def test_with_variables_1(self):
        """Test if the function returns correct dictionary with a string of variables."""
        result = Calculation('', 'x=1, y=2, z=3')
        self.assertEqual(result.variables_dict, {
                         'x': '1', ' y': '2', ' z': '3'})

    def est_with_variables_2(self):
        """Test if the function returns correct dictionary with a string of variables."""
        result = Calculation('', 'kg=1.5,meter=2,negative=-3')
        self.assertEqual(result, {'kg': '1.5', 'meter': '2', 'negative': '-3'})
