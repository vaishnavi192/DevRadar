import os
from app.services.source_classification import classify_source_role
import serpapi
from app.models.search_hypothesis import SearchHypothesis
from app.models.signal import Signal
from app.services.relevance import calculate_relevance, is_relevant


def search_google(hypothesis: SearchHypothesis) -> list[Signal]:
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        raise RuntimeError("SERPAPI_KEY is not configured")

    client = serpapi.Client(api_key=api_key)

    results = client.search(
        {
            "engine": "google",
            "q": hypothesis.query,
        }
    )

    signals = []

    for result in results.get("organic_results", []):
        title = result.get("title", "")
        url = result.get("link", "")
        snippet = result.get("snippet")

        relevance = calculate_relevance(
        product_name=hypothesis.product_name,
        query=hypothesis.query,
        title=title,
        snippet=snippet,
        url=url,
    )

        relevance_score = relevance.score

        if not is_relevant(relevance_score):
            continue

        signals.append(
            Signal(
                source="google",
                source_role=classify_source_role(url),
                signal_type=hypothesis.signal_type,
                query=hypothesis.query,
                title=title,
                url=url,
                snippet=snippet,
                relevance_score=relevance_score,
            )
        )

    return signals