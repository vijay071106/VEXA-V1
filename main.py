from core.vexa import Vexa


def main():
    vexa = Vexa()

    vexa.start()

    response1 = vexa.process("My name is V.")
    print("VEXA:", response1)

    response2 = vexa.process("What is my name?")
    print("VEXA:", response2)


if __name__ == "__main__":
    main()