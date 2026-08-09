class Vexa:
    def __init__(self):
        self.name = "VEXA"
        self.version = "1.0"

    def start(self):
        print(f"{self.name} V{self.version} is online.")
        print("Systems initialized.")


if __name__ == "__main__":
    vexa = Vexa()
    vexa.start()
    