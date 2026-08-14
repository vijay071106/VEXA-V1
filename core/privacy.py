class PrivacyCore:
    def check_external_data(self, data):
        sensitive_terms = [
            "password",
            "passwd",
            "api_key",
            "apikey",
            "secret",
            "token",
            "private_key",
            "credit_card",
        ]

        text = data.lower()

        for term in sensitive_terms:
            if term in text:
                return False

        return True