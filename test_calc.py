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

        self.calc.clear()
        self.calc.add_to_expression(15)
        self.calc.append_operator('+')
        self.calc.add_to_expression(30)
        self.calc.append_operator('+')
        self.calc.add_to_expression(405)
        self.calc.append_operator('+')
        self.calc.add_to_expression(300)
        self.calc.evaluate()
        self.assertEqual(self.calc.current_expression, '750')

    def test_subtraction(self):
        self.calc.add_to_expression(5)
        self.calc.append_operator('-')
        self.calc.add_to_expression(3)
        self.calc.evaluate()
        self.assertEqual(self.calc.current_expression, '2')

    def test_multiplication(self):
        self.calc.add_to_expression(4)
        self.calc.append_operator('*')
        self.calc.add_to_expression(2)
        self.calc.evaluate()
        self.assertEqual(self.calc.current_expression, '8')

    def test_division(self):
        self.calc.add_to_expression(8)
        self.calc.append_operator('/')
        self.calc.add_to_expression(2)
        self.calc.evaluate()
        self.assertEqual(self.calc.current_expression, '4.0')
        
    def test_combined_operations(self):
        # (5 + 3) * 2
        self.calc.add_to_expression(5)
        self.calc.append_operator('+')
        self.calc.add_to_expression(3)
        self.calc.append_operator('*')
        self.calc.add_to_expression(2)
        self.calc.evaluate()
        self.assertEqual(self.calc.current_expression, '11')

        # (10 - 2) / 4
        self.calc.clear()
        self.calc.add_to_expression(10)
        self.calc.append_operator('-')
        self.calc.add_to_expression(2)
        self.calc.append_operator('/')
        self.calc.add_to_expression(4)
        self.calc.evaluate()
        self.assertEqual(self.calc.current_expression, '2.0')
        
    def test_more_complex_expression(self):
        # 10 + 2 * 3 - 5 / 5
        self.calc.clear()
        self.calc.add_to_expression(10)
        self.calc.append_operator('+')
        self.calc.add_to_expression(2)
        self.calc.append_operator('*')
        self.calc.add_to_expression(3)
        self.calc.append_operator('-')
        self.calc.add_to_expression(5)
        self.calc.append_operator('/')
        self.calc.add_to_expression(5)
        self.calc.evaluate()
        self.assertEqual(self.calc.current_expression, '15.0') 
        
    def test_square(self):
        self.calc.add_to_expression(4)
        self.calc.square()
        self.assertEqual(self.calc.current_expression, '16')

    def test_sqrt(self):
        self.calc.add_to_expression(16)
        self.calc.sqrt()
        self.assertEqual(self.calc.current_expression, '4.0')

    def test_square_combined(self):
        # (3 + 2) ^ 2
        self.calc.add_to_expression(3)
        self.calc.append_operator('+')
        self.calc.add_to_expression(2)
        self.calc.square()
        self.assertEqual(self.calc.current_expression, '25')

    def test_sqrt_combined(self):
        # sqrt(9 + 16)
        self.calc.add_to_expression(9)
        self.calc.append_operator('+')
        self.calc.add_to_expression(16)
        self.calc.sqrt(self.calc.current_expression)
        self.assertEqual(self.calc.current_expression, '5.0')

    def test_square_root_in_expression(self):
        # (16 / 4) ^ 2
        self.calc.add_to_expression(16)
        self.calc.append_operator('/')
        self.calc.add_to_expression(4)
        self.calc.square()
        self.assertEqual(self.calc.current_expression, '16.0')

if __name__ == "__main__":
    unittest.main()
