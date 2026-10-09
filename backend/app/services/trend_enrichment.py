from app.connectors.serpapi.google_trends import get_google_trends
from app.models.evidence_cluster import EvidenceCluster
from app.models.product import Product
from app.models.trend_signal import TrendSignal


def build_trend_query(
    product: Product,
    cluster: EvidenceCluster,
) -> str | None:

    combined_text = " ".join(
        f"{item.title or ''} {item.text or ''}"
        for item in cluster.evidence
    ).lower()

    if "n8n" in combined_text:
        return f"{product.name} n8n"

    if "pagination" in combined_text:
        return f"{product.name} pagination"

    if "python" in combined_text or "sdk" in combined_text:
        return f"{product.name} Python"

    return product.name


def enrich_clusters_with_trends(
    product: Product,
    clusters: list[EvidenceCluster],
) -> list[TrendSignal]:

    trends: list[TrendSignal] = []
    seen_queries: set[str] = set()

    for cluster in clusters:
        query = build_trend_query(product, cluster)

        if not query:
            continue

        normalized_query = query.lower().strip()

        if normalized_query in seen_queries:
            continue

        seen_queries.add(normalized_query)

        try:
            trend = get_google_trends(query)
        except Exception as exc:
            print(
                f"Skipping Trends query '{query}': {exc}"
            )
            continue

        trends.append(trend)

    return trends