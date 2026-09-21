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
    def check(cls, tool_name, argument=""):
        tool_name = tool_name.lower().strip()
        argument = str(argument).lower().strip()

        # Check the tool name itself
        if cls.is_blocked(tool_name):
            return False, "Blocked: destructive actions are not allowed."

        # Check the requested operation/argument
        if cls.is_blocked(argument):
            return False, "Blocked: destructive actions are not allowed."

        return True, "Allowed."