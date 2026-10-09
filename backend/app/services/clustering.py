from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.models.evidence import Evidence
from app.models.evidence_cluster import EvidenceCluster
from app.services.evidence_classification import classify_evidence


def build_text(evidence: Evidence) -> str:
    title = evidence.title or ""
    text = evidence.text or ""

    # Don't let a long YouTube transcript dominate TF-IDF.
    text = text[:1000]

    return f"{title} {text}"


def cluster_evidence(
    evidence: list[Evidence],
    distance_threshold: float = 0.85,
) -> list[EvidenceCluster]:

    if not evidence:
        return []

    if len(evidence) == 1:
        return [
            EvidenceCluster(
                key="cluster_1",
                evidence=evidence,
            )
        ]

    texts = [build_text(item) for item in evidence]

    vectorizer = TfidfVectorizer(
        stop_words="english",
    )

    vectors = vectorizer.fit_transform(texts)

    similarities = cosine_similarity(vectors)

    # Apply a small penalty when evidence types are fundamentally different.
    classifications = [
        set(classify_evidence(item).evidence_types)
        for item in evidence
    ]

    for i in range(len(evidence)):
        for j in range(len(evidence)):
            if i == j:
                continue

            left = classifications[i]
            right = classifications[j]

            # Education and problem evidence should not be grouped
            # solely because they share vocabulary.
            if "education" in left and "problem" in right:
                similarities[i][j] *= 0.75
                similarities[j][i] *= 0.75

    distances = 1 - similarities

    model = AgglomerativeClustering(
        n_clusters=None,
        distance_threshold=distance_threshold,
        metric="precomputed",
        linkage="average",
    )

    labels = model.fit_predict(distances)

    clusters: dict[int, list[Evidence]] = {}

    for item, label in zip(evidence, labels):
        clusters.setdefault(label, []).append(item)

    return [
        EvidenceCluster(
            key=f"cluster_{index}",
            evidence=items,
        )
        for index, items in enumerate(clusters.values(), start=1)
    ]