import ollama

from config.settings import settings


class VexaBrain:
    def __init__(self):
        self.name = "VEXA Brain"
        self.model = settings.LOCAL_MODEL

    def think(self, message):
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
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )

        return response["message"]["content"]