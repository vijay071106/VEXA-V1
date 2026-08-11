class SafetyLayer:
    BLOCKED_ACTIONS = {
        "delete",
        "remove",
        "destroy",
        "format",
        "uninstall",
        "wipe",
        "erase",
    }

    @classmethod
    def is_blocked(cls, action):
        action = action.lower().strip()

        return any(
            blocked in action
            for blocked in cls.BLOCKED_ACTIONS
        )

    @classmethod
    def check(cls, action):
        if cls.is_blocked(action):
            return False, "Blocked: destructive actions are not allowed."

        return True, "Allowed."