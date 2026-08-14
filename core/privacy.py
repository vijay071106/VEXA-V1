import re

class PrivacyCore:
    def contains_email(self, data):
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        return bool(re.search(pattern, data))
    
    def contains_phone(self, data):
        pattern = r"(?<!\d)(?:\+?\d[\d\s().-]{7,}\d)(?!\d)"
        return bool(re.search(pattern, data))
    
    def contains_secret_pattern(self, data):
        patterns = [
            r"sk-[A-Za-z0-9_-]{20,}",
            r"ghp_[A-Za-z0-9]{20,}",
            r"AIza[A-Za-z0-9_-]{20,}",
        ]
        return any(re.search(pattern, data) for pattern in patterns)
    
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

        if self.contains_email(data):
            return False
        
        if self.contains_phone(data):
            return False
        
        if self.contains_secret_pattern(data):
            return False

        for term in sensitive_terms:
            if term in text:
                return False

        return True