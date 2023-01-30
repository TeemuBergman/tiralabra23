import unittest
from algorithms.shunting_yard import shunting_yard


class TestShuntingYard(unittest.TestCase):
    def test_with_empty_input(self):
        rpn = shunting_yard('')
        self.assertEqual(rpn, '')

    def test_with_basic_addition(self):
        rpn = shunting_yard('1+2')
        self.assertEqual(rpn, '1 2 +')

    def test_with_basic_subtraction(self):
        rpn = shunting_yard('1-2')
        self.assertEqual(rpn, '1 2 -')

    def test_with_basic_multiplication(self):
        rpn = shunting_yard('1*2')
        self.assertEqual(rpn, '1 2 *')

    def test_with_basic_division(self):
        rpn = shunting_yard('1/2')
        self.assertEqual(rpn, '1 2 /')

    def test_with_basic_exponentitation(self):
        rpn = shunting_yard('1^2')
        self.assertEqual(rpn, '1 2 ^')

    def test_with_basic_arithmetic_1(self):
        rpn = shunting_yard('10*(5^2)')
        self.assertEqual(rpn, '10 5 2 ^ *')

    def test_with_basic_arithmetic_2(self):
        rpn = shunting_yard('10*(5^20)/3')
        self.assertEqual(rpn, '10 5 20 ^ * 3 /')
