class ToolRouter:
    def route(self, message, is_calculation, is_web_search):
        """
        Decide which path VEXA should use.

        Returns:
            "calculator"  -> arithmetic
            "web_search"  -> web-related request
            "conversation" -> normal conversation
        """

        if is_calculation(message):
            return "calculator"

        if is_web_search(message):
            return "web_search"

        return "conversation"