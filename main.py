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

        # Tool responses are returned normally.
        # Qwen responses are already streamed by VexaBrain.
        if response and (
            vexa.brain.is_calculation(user_input)
            or vexa.brain.is_web_search(user_input)
            or user_input.lower().strip() == "privacy status"
        ):
            print(f"VEXA: {response}")


if __name__ == "__main__":
    main()