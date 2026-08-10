class CalculatorTool:
    name = "calculator"
    description = "Performs basic arithmetic calculations."

    def run(self, expression):
        try:
            allowed = "0123456789+-*/().% "

            if not all(char in allowed for char in expression):
                return "Invalid characters in expression."

            result = eval(expression, {"__builtins__": {}}, {})

            return str(result)

        except Exception:
            return "I couldn't calculate that expression."