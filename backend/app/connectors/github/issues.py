import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

from app.models.github_signal import GitHubSignal


load_dotenv()


GITHUB_API_URL = "https://api.github.com"


def search_github_issues(
    query: str,
    max_results: int = 20,
) -> list[GitHubSignal]:

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise RuntimeError("GITHUB_TOKEN is not configured")

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    response = requests.get(
        f"{GITHUB_API_URL}/search/issues",
        params={
            "q": f"{query} is:issue",
            "sort": "updated",
            "order": "desc",
            "per_page": min(max_results, 100),
        },
        headers=headers,
        timeout=15,
    )

    response.raise_for_status()

    data = response.json()

    signals = []

    for item in data.get("items", []):

        reactions = item.get("reactions", {})

        signals.append(
            GitHubSignal(
                query=query,
                title=item.get("title", ""),
                url=item.get("html_url", ""),
                body=item.get("body"),
                repository=_extract_repository(item),
                state=item.get("state"),
                created_at=item.get("created_at"),
                updated_at=item.get("updated_at"),
                comments=item.get("comments", 0),
                reactions=reactions.get("total_count", 0),
            )
        )

    return signals


def _extract_repository(item: dict) -> str:

    repository_url = item.get(
        "repository_url",
        "",
    )

    path = urlparse(repository_url).path

    parts = path.strip("/").split("/")

    if len(parts) >= 3 and parts[0] == "repos":

        owner = parts[1]
        repo = parts[2]

        return f"{owner}/{repo}"

    return "unknown"