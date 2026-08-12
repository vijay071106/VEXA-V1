import ollama

from config.settings import settings
from tools.registry import ToolRegistry


class VexaBrain:
    def __init__(self):
        self.name = "VEXA Brain"
        self.model = settings.LOCAL_MODEL
        self.history = []
        self.tool_registry = ToolRegistry()

    def use_tool(self, name, argument):
        return self.tool_registry.execute(name, argument)

    def decide_tool(self, message):
        response = ollama.chat(
            model=self.model,
            format="json",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are VEXA's tool decision system. "
                        "Available tool: calculator. "
                        "If the user needs arithmetic, return JSON with "
                        "'action' set to 'calculator' and 'argument' containing "
                        "the arithmetic expression. "
                        "Otherwise return JSON with 'action' set to 'answer' "
                        "and 'argument' set to an empty string. "
                        "Return JSON only."
                    ),
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )

        return response["message"]["content"]

    def is_calculation(self, message):
        allowed = "0123456789+-*/().% "

        cleaned = (
            message.lower()
            .replace("what is", "")
            .replace("calculate", "")
            .replace("?", "")
            .strip()
        )

        return bool(cleaned) and all(
            char in allowed for char in cleaned
        )

    def is_web_search(self, message):
        triggers = [
            "search for",
            "search",
            "look up",
            "find online",
            "google",
            "what happened today",
            "latest news",
            "current news",
        ]
        message = message.lower().strip()
        return any(trigger in message for trigger in triggers)

    def think(self, message):
        # Check for simple arithmetic expressions first
        if self.is_calculation(message):
            expression = (
                message.lower()
                .replace("what is", "")
                .replace("calculate", "")
                .replace("?", "")
                .strip()
            )

            result = self.use_tool("calculator", expression)
            return result

        # Check if user is asking for a web search
        def is_web_search(self, message):
            message = message.lower().strip()
            triggers = [
                "search for",
                "search",
                "look up",
                "find online",
                "google",
                "what happened today",
                "latest news",
                "current news",
            ]
            question_starts = [
                "what ",
                "where ",
                "when ",
                "who ",
            ]
            if any(trigger in message for trigger in triggers):
                return True
            if any(message.startswith(start) for start in question_starts):
                return True

            return False
        return self.use_tool("web_search", query)

        # Fallback: normal conversational response
        self.history.append({
            "role": "user",
            "content": message,
        })

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are VEXA, a personal AI assistant. "
                        "Always respond in English unless the user requests "
                        "another language. Be concise, helpful, and natural."
                    ),
                },
                *self.history,
            ],
            stream=True,
        )
        reply = ""

        for chunk in response:
            text = chunk["message"]["content"]
            print(text, end="", flush=True)
            reply += text

        print()

        self.history.append({
            "role": "assistant",
            "content": reply,
        })

        return reply