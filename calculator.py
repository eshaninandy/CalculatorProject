class CalculatorCLI:
    def __init__(self):
        self.total_expression = ""
        self.current_expression = ""

    def add_to_expression(self, value):
        self.current_expression += str(value)

    def append_operator(self, operator):
        self.total_expression += self.current_expression + operator
        self.current_expression = ""

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))

    def evaluate(self):
        self.total_expression += self.current_expression
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception:
            self.current_expression = "Error"

    def run(self):
        print("CLI Calculator (type 'exit' to quit)")
        while True:
            command = input("Enter a number, operator, or command: ").strip()
            if command == "exit":
                break
            elif command.isdigit() or command == ".":
                self.add_to_expression(command)
            elif command in "+-*/":
                self.append_operator(command)
            elif command == "=":
                self.evaluate()
                print("Result:", self.current_expression)
            elif command == "C":
                self.clear()
            elif command == "square":
                self.square()
                print("Square:", self.current_expression)
            elif command == "sqrt":
                self.sqrt()
                print("Square root:", self.current_expression)
            else:
                print("Invalid input")


if __name__ == "__main__":
    calc = CalculatorCLI()
    calc.run()
