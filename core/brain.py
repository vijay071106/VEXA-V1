from openai import OpenAI

from config.settings import settings


class VexaBrain:
    def __init__(self):
        self.name = "VEXA Brain"
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def think(self, message):
        response = self.client.responses.create(
            model="gpt-5-mini",
            input=message
        )

        return response.output_text