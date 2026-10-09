import unittest

from app.models.evidence_cluster import EvidenceCluster
from app.models.signal import Signal
from app.services.evidence_selection import select_evidence


def signal(
    *,
    url: str,
    source_role: str,
    relevance_score: float,
) -> Signal:
    return Signal(
        source="google",
        source_role=source_role,
        signal_type="developer_demand",
        query="SerpApi python",
        title=f"Evidence from {url}",
        url=url,
        snippet="Relevant developer evidence.",
        relevance_score=relevance_score,
    )


def cluster(signals: list[Signal]) -> EvidenceCluster:
    return EvidenceCluster(
        key="python_implementation",
        intent="implementation",
        signal_type="developer_demand",
        signals=signals,
    )


class EvidenceSelectionTests(unittest.TestCase):
    def test_excludes_low_relevance_results(self):
        evidence = select_evidence(
            cluster(
                [
                    signal(
                        url="https://stackoverflow.com/questions/1",
                        source_role="community",
                        relevance_score=0.80,
                    ),
                    signal(
                        url="https://example.com/weak",
                        source_role="third_party",
                        relevance_score=0.29,
                    ),
                ]
            )
        )

        self.assertEqual([item.url for item in evidence], [
            "https://stackoverflow.com/questions/1"
        ])

    def test_limits_selection_to_five_signals(self):
        evidence = select_evidence(
            cluster(
                [
                    signal(
                        url=f"https://publisher-{index}.example.com/article",
                        source_role="third_party",
                        relevance_score=0.90 - index / 100,
                    )
                    for index in range(6)
                ]
            )
        )

        self.assertEqual(len(evidence), 5)

    def test_reduces_repeated_domains_when_alternatives_exist(self):
        evidence = select_evidence(
            cluster(
                [
                    signal(
                        url="https://serpapi.com/article-1",
                        source_role="first_party",
                        relevance_score=0.90,
                    ),
                    signal(
                        url="https://serpapi.com/article-2",
                        source_role="first_party",
                        relevance_score=0.85,
                    ),
                    signal(
                        url="https://stackoverflow.com/questions/1",
                        source_role="community",
                        relevance_score=0.80,
                    ),
                    signal(
                        url="https://publisher.example.com/article",
                        source_role="third_party",
                        relevance_score=0.75,
                    ),
                ]
            )
        )

        domains = [item.url.split("/")[2] for item in evidence]
        self.assertEqual(domains.count("serpapi.com"), 1)

    def test_preserves_source_roles_and_first_party_context(self):
        evidence = select_evidence(
            cluster(
                [
                    signal(
                        url="https://github.com/example/repo",
                        source_role="community",
                        relevance_score=0.90,
                    ),
                    signal(
                        url="https://publisher.example.com/article",
                        source_role="third_party",
                        relevance_score=0.80,
                    ),
                    signal(
                        url="https://serpapi.com/docs/python",
                        source_role="first_party",
                        relevance_score=0.70,
                    ),
                ]
            )
        )

        self.assertEqual(
            {item.source_role for item in evidence},
            {"community", "third_party", "first_party"},
        )

    def test_selection_is_deterministic(self):
        signals = [
            signal(
                url="https://serpapi.com/docs/python",
                source_role="first_party",
                relevance_score=0.70,
            ),
            signal(
                url="https://github.com/example/repo",
                source_role="community",
                relevance_score=0.80,
            ),
            signal(
                url="https://publisher.example.com/article",
                source_role="third_party",
                relevance_score=0.75,
            ),
        ]

        selected = select_evidence(cluster(signals))
        reversed_selected = select_evidence(cluster(list(reversed(signals))))

        self.assertEqual(
            [item.url for item in selected],
            [item.url for item in reversed_selected],
        )


if __name__ == "__main__":
    unittest.main()
