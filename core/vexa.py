from config.settings import settings


class Vexa:
    def __init__(self):
        self.name = settings.APP_NAME
        self.version = settings.APP_VERSION

    def start(self):
        print(f"{self.name} V{self.version} is online.")
        print("Systems initialized.")


if __name__ == "__main__":
    vexa = Vexa()
    vexa.start()
    