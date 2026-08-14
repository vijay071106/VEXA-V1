from datetime import datetime
import json
from pathlib import Path


class ActivityLog:
    def __init__(self, file_path="data/activity_log.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if self.file_path.exists():
            try:
                self.events = json.loads(
                    self.file_path.read_text(encoding="utf-8")
                )
            except (json.JSONDecodeError, OSError):
                self.events = []
        else:
            self.events = []

    def record(self, action, status):
        allowed_statuses = {"ALLOWED", "BLOCKED"}
        if status not in allowed_statuses:
            status = "BLOCKED"
            event = {
                "time": datetime.now().isoformat(timespec="seconds"),
                "action": action,
                "status": status,
            }

    def recent(self, limit=10):
        return self.events[-limit:]
    
    def display_recent(self, limit=10):
        for event in self.recent(limit):
            print(
                f"[{event['time']}] "
                f"{event['action']} → {event['status']}"
            )