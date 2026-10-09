from app.models.developer_problem import DeveloperProblem
from app.models.evidence_cluster import EvidenceCluster
from app.services.evidence_classification import classify_evidence


def _has_problem_evidence(
    cluster: EvidenceCluster,
) -> bool:
    return any(
        "problem" in classify_evidence(item).evidence_types
        for item in cluster.evidence
    )


def build_problem_candidates(
    clusters: list[EvidenceCluster],
) -> list[EvidenceCluster]:
    return [
        cluster
        for cluster in clusters
        if _has_problem_evidence(cluster)
    ]