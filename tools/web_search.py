import requests


class WebSearchTool:
    name = "web_search"
    description = "Searches the web for information."

    def run(self, query):
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
                results.append(data["AbstractText"])

            for topic in data.get("RelatedTopics", [])[:5]:
                if isinstance(topic, dict) and topic.get("Text"):
                    results.append(topic["Text"])

            if not results:
                return "No useful results found."

            return "\n".join(results)

        except requests.RequestException:
            return "Web search is currently unavailable."