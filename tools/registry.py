from tools.calculator import CalculatorTool


class ToolRegistry:
    def __init__(self):
        self.tools = {
            "calculator": CalculatorTool(),
        }

    def get_tool(self, name):
        return self.tools.get(name)

    def list_tools(self):
        return list(self.tools.keys())