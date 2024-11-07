import unittest
from calculator import CalculatorCLI  # import your class/module as needed

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = CalculatorCLI()

    def test_addition(self):
        self.calc.add_to_expression(5)
        self.calc.append_operator('+')
        self.calc.add_to_expression(3)
        self.calc.evaluate()
        self.assertEqual(self.calc.current_expression, '8')

    def test_subtraction(self):
        self.calc.add_to_expression(5)
        self.calc.append_operator('-')
        self.calc.add_to_expression(3)
        self.calc.evaluate()
        self.assertEqual(self.calc.current_expression, '2')

    # Add more tests for subtraction, multiplication, division, etc.

if __name__ == "__main__":
    unittest.main()
