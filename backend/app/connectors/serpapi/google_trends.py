import os

import serpapi
from dotenv import load_dotenv

from app.models.trend_signal import TrendSignal

load_dotenv()


def get_google_trends(query: str) -> TrendSignal:
    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        raise RuntimeError("SERPAPI_KEY is not configured")

    client = serpapi.Client(api_key=api_key)

    timeline_results = client.search(
        {
            "engine": "google_trends",
            "q": query,
            "date": "today 12-m",
            "geo": "US",
            "hl": "en",
            "data_type": "TIMESERIES",
        }
    )

    topics_results = client.search(
        {
            "engine": "google_trends",
            "q": query,
            "date": "today 12-m",
            "geo": "US",
            "hl": "en",
            "data_type": "RELATED_TOPICS",
        }
    )

    queries_results = client.search(
        {
            "engine": "google_trends",
            "q": query,
            "date": "today 12-m",
            "geo": "US",
            "hl": "en",
            "data_type": "RELATED_QUERIES",
        }
    )

    if timeline_results.get("error"):
        raise RuntimeError(
            f"Google Trends timeseries error: {timeline_results['error']}"
        )

    interest_over_time = _extract_interest_over_time(timeline_results)

    if topics_results.get("error"):
            related_topics = []
    else:
            related_topics = _extract_related_topics(topics_results)

    if queries_results.get("error"):
            related_queries = []
    else:
            related_queries = _extract_related_queries(queries_results)

    trend_direction = _determine_trend_direction(interest_over_time)

    return TrendSignal(
            query=query,
            trend_direction=trend_direction,
            interest_over_time=interest_over_time,
            related_topics=related_topics,
            related_queries=related_queries,
        )
    
def _extract_related_topics(results: dict) -> list[str]:
    related_topics = results.get("related_topics", {})

    topics = []

    for section in ("rising", "top"):
        for item in related_topics.get(section, []):
            if not isinstance(item, dict):
                continue

            topic = item.get("topic", {})

            if not isinstance(topic, dict):
                continue

            title = topic.get("title")

            if title and title not in topics:
                topics.append(title)

    return topics[:10]


def _extract_related_queries(results: dict) -> list[str]:
    related_queries = results.get("related_queries", {})

    queries = []

    for section in ("rising", "top"):
        for item in related_queries.get(section, []):
            if not isinstance(item, dict):
                continue

            query = item.get("query")

            if query and query not in queries:
                queries.append(query)

    return queries[:10]


def _determine_trend_direction(
    timeline: list[dict],
) -> str:

    values = []

    for item in timeline:
        for value in item.get("values", []):
            if not isinstance(value, dict):
                continue

            extracted_value = value.get("extracted_value")

            if isinstance(extracted_value, (int, float)):
                values.append(extracted_value)

    if len(values) < 4:
        return "unknown"

    midpoint = len(values) // 2

    first_half = values[:midpoint]
    second_half = values[midpoint:]

    first_average = sum(first_half) / len(first_half)
    second_average = sum(second_half) / len(second_half)

    difference = second_average - first_average

    if difference > 10:
        return "rising"

    if difference < -10:
        return "declining"

    return "stable"

def _extract_interest_over_time(results: dict) -> list[dict]:
    interest = results.get("interest_over_time", {})

    timeline = interest.get("timeline_data", [])

    return [
        {
            "date": item.get("date"),
            "values": item.get("values", []),
        }
        for item in timeline
    ]
    