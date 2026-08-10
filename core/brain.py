import ollama

from config.settings import settings


class VexaBrain:
    def __init__(self):
        self.name = "VEXA Brain"
        self.model = settings.LOCAL_MODEL
        self.history = []

    def think(self, message):
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
        )

        reply = response["message"]["content"]

        self.history.append({
            "role": "assistant",
            "content": reply,
        })

        return reply