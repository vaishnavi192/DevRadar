from app.models.product import Product

from app.services.research import build_research_packet
from app.services.evidence_normalization import normalize_research_packet
from app.services.deduplication import deduplicate_evidence
from app.services.evidence_filter import filter_evidence
from app.services.clustering import cluster_evidence
from app.services.trend_enrichment import enrich_clusters_with_trends
from app.services.llm.gemini import synthesize_research


product = Product(
    name="SerpApi",
    website="https://serpapi.com",
    targetAudience="Developers",
)


# 1. Initial research
packet = build_research_packet(product)

print("Google signals:", len(packet.google_search))
print("YouTube signals:", len(packet.youtube))
print("GitHub signals:", len(packet.github))


# 2. Normalize
evidence = normalize_research_packet(packet)

print("Normalized:", len(evidence))


# 3. Deduplicate
evidence = deduplicate_evidence(evidence)

print("After deduplication:", len(evidence))


# 4. Filter
evidence = filter_evidence(evidence)

print("After filtering:", len(evidence))


# 5. Cluster
clusters = cluster_evidence(evidence)

print("Clusters:", len(clusters))

for cluster in clusters:
    print(
        f"{cluster.key}: "
        f"{len(cluster.evidence)} evidence items"
    )


# 6. Trends
trend_signals = enrich_clusters_with_trends(
    product=product,
    clusters=clusters,
)

print("Trend signals:", len(trend_signals))

for trend in trend_signals:
    print(
        f"Trend: {trend.query} "
        f"→ {trend.trend_direction}"
    )


# 7. Final Gemini synthesis
result = synthesize_research(
    product=product,
    clusters=clusters,
    trends=trend_signals,
)


print("\n=== DEVELOPER PROBLEMS ===")

for problem in result.developer_problems:
    print(f"\nTitle: {problem.title}")
    print(f"Problem: {problem.is_problem}")
    print(f"Confidence: {problem.confidence}")
    print(f"Conclusion: {problem.conclusion}")
    print(f"Evidence count: {problem.evidence_count}")
    print(f"Sources: {problem.source_breakdown}")
    print(f"Supporting evidence: {problem.supporting_evidence}")
    print(f"Limitations: {problem.limitations}")


print("\n=== CONCLUSIONS ===")

for conclusion in result.conclusions:
    print(f"- {conclusion}")


print("\n=== DEMAND SIGNALS ===")

for signal in result.demand_signals:
    print(f"\nQuery: {signal.query}")
    print(f"Direction: {signal.direction}")
    print(f"Interpretation: {signal.interpretation}")
    print(f"Limitations: {signal.limitations}")


print("\n=== CONTENT GAPS ===")

for gap in result.content_gaps:
    print(f"\nTopic: {gap.topic}")
    print(f"Reason: {gap.reason}")
    print(f"Evidence: {gap.evidence}")


print("\n=== GTM RECOMMENDATIONS ===")

for recommendation in result.gtm_recommendations:
    print(f"\nRecommendation: {recommendation.recommendation}")
    print(f"Reason: {recommendation.reason}")
    print(f"Priority: {recommendation.priority}")