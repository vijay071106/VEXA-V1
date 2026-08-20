from tools.safety import SafetyLayer
from tools.calculator import CalculatorTool
from tools.web_search import WebSearchTool


class ToolRegistry:
    def __init__(self, kill_switch):
        self.tools = {
            "calculator": {
                "tool": CalculatorTool(),
                "risk": "safe",
            },
            "web_search": {
                "tool": WebSearchTool(kill_switch),
                "risk": "safe",
            },
        }

    def get_tool(self, name):
        entry = self.tools.get(name)

        if entry is None:
            return None

        return entry["tool"]

    def list_tools(self):
        return list(self.tools.keys())

    def get_risk(self, name):
        entry = self.tools.get(name)

        if entry is None:
            return None

        return entry["risk"]

    def execute(self, name, argument):
        allowed, message = SafetyLayer.check(name)

        if not allowed:
            return message

        tool = self.get_tool(name)

        if tool is None:
            return f"Tool '{name}' is not available."

        return tool.run(argument)