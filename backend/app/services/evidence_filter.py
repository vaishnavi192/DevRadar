from app.models.evidence import Evidence


def filter_evidence(
    evidence: list[Evidence],
    min_relevance: float = 0.30,
) -> list[Evidence]:
    return [
        item
        for item in evidence
        if item.relevance_score >= min_relevance
    ]