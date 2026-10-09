from urllib.parse import urlparse

from app.connectors.github.issues import search_github_issues
from app.models.github_signal import GitHubSignal
from app.models.product import Product
from app.services.github_relevance import (
    github_relevance_score,
    github_source_role,
    is_useful_github_signal,
)


MAX_RESULTS_PER_QUERY = 10
MAX_FINAL_RESULTS = 10


PROBLEM_TERMS = [
    "error",
    "bug",
    "problem",
    "issue",
    "broken",
    "failure",
    "pagination",
    "authentication",
    "integration",
    "sdk",
    "documentation",
    "rate limit",
]


GITHUB_TEMPLATE_PATTERNS = [
    "short summary of the bug",
    "omit if not an api",
    "please describe the bug",
    "please describe the problem",
    "steps to reproduce",
]


def _github_owner(github_url: str | None) -> str | None:
    if not github_url:
        return None

    parsed = urlparse(github_url)
    parts = parsed.path.strip("/").split("/")

    if not parts:
        return None

    return parts[0]


def _build_queries(product: Product) -> list[str]:
    queries: list[str] = []

    # Community evidence.
    #
    # Requiring the product name in the issue title
    # prevents issues that merely mention the product
    # somewhere in a large body from dominating results.
    for term in PROBLEM_TERMS:
        queries.append(
            f'"{product.name}" in:title {term}'
        )

    # First-party evidence.
    #
    # If the product has a GitHub organization/user URL,
    # search that owner directly.
    owner = _github_owner(product.github_url)

    if owner:
        for term in PROBLEM_TERMS:
            queries.append(
                f"org:{owner} {term}"
            )

    return queries


def is_template_issue(signal: GitHubSignal) -> bool:
    """
    Detect GitHub issue-template/example issues that are
    not actual developer problems.
    """

    title = signal.title.lower()

    return any(
        pattern in title
        for pattern in GITHUB_TEMPLATE_PATTERNS
    )


def research_github(
    product: Product,
    max_final_results: int = MAX_FINAL_RESULTS,
) -> list[GitHubSignal]:

    signals_by_url: dict[str, GitHubSignal] = {}

    queries = _build_queries(product)

    for query in queries:

        results = search_github_issues(
            query=query,
            max_results=MAX_RESULTS_PER_QUERY,
        )

        for signal in results:

            # Ignore results without a URL.
            if not signal.url:
                continue

            # Ignore obvious GitHub issue-template/example issues.
            if is_template_issue(signal):
                continue

            if not is_useful_github_signal(
                signal=signal,
                product_name=product.name,
            ):
                continue

            # Deduplicate the same GitHub issue returned
            # by multiple queries.
            if signal.url in signals_by_url:
                continue

            relevance_score = github_relevance_score(
                signal=signal,
                product_name=product.name,
            )

            source_role = github_source_role(
                repository=signal.repository,
                github_url=product.github_url,
            )

            enriched = signal.model_copy(
                update={
                    "relevance_score": relevance_score,
                    "source_role": source_role,
                }
            )

            signals_by_url[signal.url] = enriched

    candidates = list(signals_by_url.values())

    # Remove weak results.
    candidates = [
        signal
        for signal in candidates
        if signal.relevance_score >= 0.30
    ]

    # Rank by relevance first.
    # Engagement is only a secondary signal.
    candidates.sort(
        key=lambda signal: (
            -signal.relevance_score,
            -signal.comments,
            -signal.reactions,
            signal.url,
        )
    )

    return candidates[:max_final_results]