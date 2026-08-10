from core.vexa import Vexa


def main():
    vexa = Vexa()
    vexa.start()

    print("Type 'exit' to stop VEXA.")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("VEXA shutting down.")
            break

        if not user_input:
            continue

        response = vexa.process(user_input)
        print(f"VEXA: {response}")


if __name__ == "__main__":
    main()