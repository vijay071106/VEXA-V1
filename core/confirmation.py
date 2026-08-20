class ConfirmationManager:
    def request_confirmation(self, action):
        answer = input(
            f"VEXA wants to perform: {action}. Confirm? [y/n]: "
        )

        return answer.lower().strip() == "y"