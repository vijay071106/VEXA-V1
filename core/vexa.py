from config.settings import settings
from core.brain import VexaBrain


class Vexa:
    def __init__(self):
        self.name = settings.APP_NAME
        self.version = settings.APP_VERSION
        self.brain = VexaBrain()

    def start(self):
        print(f"{self.name} V{self.version} is online.")
        print("Systems initialized.")
        

    def process(self, message):
        return self.brain.think(message)