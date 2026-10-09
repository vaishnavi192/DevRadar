from urllib.parse import urlparse

from app.models.github_signal import GitHubSignal


PROBLEM_TERMS = {
    "error",
    "bug",
    "issue",
    "problem",
    "broken",
    "failure",
    "failed",
    "incorrect",
    "wrong",
    "missing",
    "not working",
    "doesn't work",
    "does not work",
    "unexpected",
    "timeout",
    "rate limit",
}


def github_source_role(
    repository: str,
    github_url: str | None,
) -> str:

    if not github_url:
        return "community"

    parsed = urlparse(github_url)

    parts = parsed.path.strip("/").split("/")

    if not parts:
        return "community"

    product_owner = parts[0].lower()

    repository_parts = repository.split("/")

    if not repository_parts:
        return "community"

    repository_owner = repository_parts[0].lower()

    if repository_owner == product_owner:
        return "first_party"

    return "community"


def normalize_text(value: str | None) -> str:
    if not value:
        return ""

    return " ".join(value.lower().split())


def github_relevance_score(
    signal: GitHubSignal,
    product_name: str,
) -> float:

    title = normalize_text(signal.title)
    body = normalize_text(signal.body)
    product_name = normalize_text(product_name)

    score = 0.0

    # Strong signal:
    # product name appears in the title.
    if product_name and product_name in title:
        score += 0.60

    # Weaker signal:
    # product name appears only in the body.
    elif product_name and product_name in body:
        score += 0.20

    # Problem language in the title.
    title_problem_matches = sum(
        1
        for term in PROBLEM_TERMS
        if term in title
    )

    if title_problem_matches:
        score += 0.20

    # Problem language in the body.
    body_problem_matches = sum(
        1
        for term in PROBLEM_TERMS
        if term in body
    )

    if body_problem_matches:
        score += min(
            body_problem_matches * 0.03,
            0.10,
        )

    # Weak engagement signals.
    if signal.comments >= 5:
        score += 0.05

    if signal.reactions >= 3:
        score += 0.05

    return round(min(score, 1.0), 2)

def is_useful_github_signal(
    signal: GitHubSignal,
    product_name: str,
) -> bool:

    title = normalize_text(signal.title)
    body = normalize_text(signal.body)
    product_name = normalize_text(product_name)

    # Product should be explicitly associated with the issue.
    product_in_title = product_name in title
    product_in_body = product_name in body

    if not product_in_title and not product_in_body:
        return False

    # Reject obvious "alternatives" / comparison content.
    exclusion_terms = {
        "alternative",
        "alternatives",
        "comparison",
        "compare",
        "versus",
        "vs",
    }

    if any(term in title for term in exclusion_terms):
        return False

    # Require actual problem language somewhere.
    problem_matches = sum(
        1
        for term in PROBLEM_TERMS
        if term in title or term in body
    )

    if problem_matches == 0:
        return False

    return True