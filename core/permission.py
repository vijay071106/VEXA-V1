class PermissionManager:
    def __init__(self):
        self.external_access = False

    def request_external_access(self):
        answer = input("VEXA wants to access the internet. Allow? [y/n]: ")
        self.external_access = answer.lower().strip() == "y"
        return self.external_access

    def is_allowed(self):
        return self.external_access

    def revoke(self):
        self.external_access = False