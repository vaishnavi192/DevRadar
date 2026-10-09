from urllib.parse import urlparse

from app.models.evidence import Evidence
from app.models.evidence_cluster import EvidenceCluster


MAX_EVIDENCE_PER_CLUSTER = 5

_SOURCE_ROLE_PRIORITY = {
    "community": 0,
    "third_party": 1,
    "first_party": 2,
}


def _normalized_domain(url: str) -> str:
    """Return a stable domain key for simple duplicate-domain filtering."""
    domain = urlparse(url).netloc.lower().removeprefix("www.")
    return domain or url.lower()


def _evidence_sort_key(
    evidence: Evidence,
) -> tuple[float, int, str, str, str]:
    """Rank evidence by relevance, then stable tie-breakers."""
    return (
        -evidence.relevance_score,
        _SOURCE_ROLE_PRIORITY.get(evidence.source_role, 1),
        _normalized_domain(evidence.url),
        evidence.url.lower(),
        evidence.title.lower(),
    )


def _source_roles(evidence: list[Evidence]) -> list[str]:
    return sorted(
        {item.source_role for item in evidence},
        key=lambda role: (
            _SOURCE_ROLE_PRIORITY.get(role, 1),
            role,
        ),
    )


def select_evidence(
    cluster: EvidenceCluster,
    max_evidence: int = MAX_EVIDENCE_PER_CLUSTER,
) -> list[Evidence]:
    """
    Select a compact and diverse evidence set from one cluster.

    Selection strategy:
    1. Keep only relevant evidence.
    2. Prefer the strongest evidence by relevance.
    3. Preserve source-role diversity.
    4. Avoid repeated domains.
    5. Limit first-party evidence when independent evidence exists.
    """
    if max_evidence <= 0:
        return []

    candidates = sorted(
    cluster.evidence,
    key=_evidence_sort_key,
)

    selected: list[Evidence] = []
    selected_domains: set[str] = set()
    selected_ids: set[int] = set()

    has_independent_evidence = any(
        item.source_role != "first_party"
        for item in candidates
    )

    first_party_count = 0

    def can_select(item: Evidence) -> bool:
        nonlocal first_party_count

        domain = _normalized_domain(item.url)

        if id(item) in selected_ids:
            return False

        if domain in selected_domains:
            return False

        if (
            item.source_role == "first_party"
            and has_independent_evidence
            and first_party_count >= 1
        ):
            return False

        selected.append(item)
        selected_ids.add(id(item))
        selected_domains.add(domain)

        if item.source_role == "first_party":
            first_party_count += 1

        return True

    # First pass: preserve source-role diversity.
    for role in _source_roles(candidates):
        for item in candidates:
            if item.source_role == role and can_select(item):
                break

        if len(selected) == max_evidence:
            return selected

    # Second pass: fill remaining slots by relevance.
    for item in candidates:
        can_select(item)

        if len(selected) == max_evidence:
            break

    return selected