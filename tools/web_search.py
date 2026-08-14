import requests
from core.privacy import PrivacyCore

class WebSearchTool:
    name = "web_search"
    description = "Searches the web for information."
    
    def __init__(self):
        self.privacy = PrivacyCore()

    def run(self, query):
        if not self.privacy.check_external_data(query):
            return "I cannot search for that."

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