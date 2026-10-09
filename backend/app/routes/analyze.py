from fastapi import APIRouter

from app.models.product import Product
from app.services.clustering import cluster_evidence
from app.services.deduplication import deduplicate_evidence
from app.services.evidence_filter import filter_evidence
from app.services.evidence_normalization import normalize_research_packet
from app.services.llm.gemini import synthesize_research
from app.services.research import build_research_packet
from app.services.trend_enrichment import enrich_clusters_with_trends


router = APIRouter()


@router.post("/analyze")
def analyze(product: Product):

    packet = build_research_packet(product)

    evidence = normalize_research_packet(packet)

    evidence = deduplicate_evidence(evidence)

    evidence = filter_evidence(evidence)

    clusters = cluster_evidence(evidence)

    trends = enrich_clusters_with_trends(
        product=product,
        clusters=clusters,
    )

    result = synthesize_research(
        product=product,
        clusters=clusters,
        trends=trends,
    )

    return result
