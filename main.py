from core.vexa import Vexa


def main():
    vexa = Vexa()

    vexa.start()

    response = vexa.process("Hello VEXA")
    print(response)


if __name__ == "__main__":
    main()