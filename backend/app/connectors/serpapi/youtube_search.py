import os

import serpapi

from app.models.youtube_signal import YouTubeSignal
from app.services.relevance import calculate_relevance
from dotenv import load_dotenv


load_dotenv()

def search_youtube(
    query: str,
    product_name: str,
    max_results: int = 10,
) -> list[YouTubeSignal]:

    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        raise RuntimeError("SERPAPI_KEY is not configured")

    client = serpapi.Client(api_key=api_key)

    results = client.search(
        {
            "engine": "youtube",
            "search_query": query,
        }
    )

    signals = []

    for result in results.get("video_results", [])[:max_results]:

        video_id = result.get("video_id")

        if not video_id:
            continue

        title = result.get("title", "")

        snippet = (
            result.get("description")
            or result.get("snippet")
        )

        url = result.get(
            "link",
            f"https://www.youtube.com/watch?v={video_id}",
        )

        relevance = calculate_relevance(
        product_name=product_name,
        query=query,
        title=title,
        snippet=snippet,
        url=url,
)

        relevance_score = relevance.score

        channel = result.get("channel")

        if isinstance(channel, dict):
            channel = channel.get("name")

        signals.append(
            YouTubeSignal(
                query=query,
                video_id=video_id,
                title=title,
                url=url,
                snippet=snippet,
                channel=channel,
                published_at=result.get("published_date"),
                views=_parse_int(result.get("views")),
                likes=_parse_int(result.get("likes")),
                comments=_parse_int(result.get("comments")),
                relevance_score=relevance_score,
            )
        )

    return signals


def _parse_int(value) -> int | None:

    if value is None:
        return None

    if isinstance(value, int):
        return value

    try:
        return int(value)
    except (TypeError, ValueError):
        return None