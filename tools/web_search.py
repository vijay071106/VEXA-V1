import requests

from core.privacy import PrivacyCore
from core.activity_log import ActivityLog
from core.permission import PermissionManager
from core.confirmation import ConfirmationManager


class WebSearchTool:
    name = "web_search"
    description = "Searches the web for information."

    def __init__(self):
        self.privacy = PrivacyCore()
        self.activity_log = ActivityLog()
        self.permission = PermissionManager()
        self.confirmation = ConfirmationManager()

    def run(self, query):
        # 1. Check privacy first
        if not self.privacy.check_external_data(query):
            self.activity_log.record("WEB_SEARCH", "BLOCKED")
            return "I cannot search for that."

        # 2. Ask for internet permission if not already granted
        if not self.permission.is_allowed():
            if not self.permission.request_external_access():
                self.activity_log.record("WEB_SEARCH", "BLOCKED")
                return "Internet access is not permitted."

        # 3. Ask for explicit confirmation
        if not self.confirmation.request_confirmation("WEB_SEARCH"):
            self.activity_log.record("WEB_SEARCH", "BLOCKED")
            return "Web search cancelled."

        # 4. Log the approved action
        self.activity_log.record("WEB_SEARCH", "ALLOWED")

        try:
            response = requests.get(
                "https://api.duckduckgo.com/",
                params={
                    "q": query,
                    "format": "json",
                    "no_html": 1,
                    "skip_disambig": 1,
                },
                timeout=10,
            )

            response.raise_for_status()
            data = response.json()

            results = []

            if data.get("AbstractText"):
                results.append(
                    f"Summary: {data['AbstractText'][:400]}"
                )

            for topic in data.get("RelatedTopics", [])[:3]:
                if isinstance(topic, dict) and topic.get("Text"):
                    results.append(
                        f"- {topic['Text'][:200]}"
                    )

            if not results:
                return "No useful results found."

            return "\n\n".join(results)

        except requests.RequestException:
            return "Web search is currently unavailable."