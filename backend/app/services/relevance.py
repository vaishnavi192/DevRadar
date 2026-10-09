import re
from urllib.parse import urlparse

from pydantic import BaseModel


DEVELOPER_DOMAINS = {
    "github.com",
    "stackoverflow.com",
    "gitlab.com",
    "bitbucket.org",
    "dev.to",
    "hashnode.com",
}

DEVELOPER_TERMS = {
    "api",
    "sdk",
    "python",
    "javascript",
    "typescript",
    "node",
    "nodejs",
    "integration",
    "developer",
    "code",
    "library",
    "package",
    "endpoint",
    "request",
    "response",
    "authentication",
    "authorization",
    "webhook",
    "scraping",
    "scraper",
    "pagination",
    "query",
    "json",
}

PROBLEM_TERMS = {
    "error",
    "exception",
    "failed",
    "failure",
    "broken",
    "issue",
    "problem",
    "bug",
    "incorrect",
    "invalid",
    "missing",
    "unable",
    "timeout",
    "crash",
    "doesn't work",
    "not working",
    "cannot",
    "can't",
}

TECHNICAL_PATTERNS = [
    r"\bHTTP\s?[45]\d{2}\b",
    r"\b[45]\d{2}\s+(error|status)\b",
    r"\b[A-Z][A-Za-z]+Error\b",
    r"\bAPI\s+key\b",
    r"\bapi_key\b",
    r"\btimeout\b",
    r"\bexception\b",
    r"\bstack\s*trace\b",
]


class RelevanceResult(BaseModel):
    score: float
    product_relevance: float
    developer_relevance: float
    problem_relevance: float
    source_quality: float
    technical_specificity: float


def normalize_text(value: str | None) -> str:
    if not value:
        return ""

    return re.sub(r"\s+", " ", value.lower()).strip()


def tokenize(value: str | None) -> set[str]:
    return set(
        re.findall(
            r"[a-z0-9]+",
            normalize_text(value),
        )
    )


def combined_text(
    title: str,
    snippet: str | None,
) -> str:
    return normalize_text(
        f"{title} {snippet or ''}"
    )


def product_match_score(
    product_name: str,
    title: str,
    snippet: str | None,
) -> float:
    product_tokens = tokenize(product_name)
    title_tokens = tokenize(title)
    snippet_tokens = tokenize(snippet)

    if not product_tokens:
        return 0.0

    title_matches = product_tokens & title_tokens
    snippet_matches = product_tokens & snippet_tokens

    score = 0.0

    if title_matches == product_tokens:
        score += 0.70
    elif title_matches:
        score += 0.40

    if snippet_matches:
        score += 0.30

    return min(score, 1.0)


def developer_relevance_score(
    title: str,
    snippet: str | None,
) -> float:
    text = combined_text(title, snippet)

    if not text:
        return 0.0

    tokens = tokenize(text)
    matches = tokens & DEVELOPER_TERMS

    if not matches:
        return 0.0

    # More distinct developer terms means stronger developer relevance.
    return min(len(matches) / 5, 1.0)


def problem_relevance_score(
    title: str,
    snippet: str | None,
) -> float:
    text = combined_text(title, snippet)

    if not text:
        return 0.0

    tokens = tokenize(text)

    # Handle multi-word problem terms separately.
    token_matches = tokens & PROBLEM_TERMS

    phrase_matches = [
        term
        for term in PROBLEM_TERMS
        if " " in term and term in text
    ]

    total_matches = len(token_matches) + len(phrase_matches)

    if total_matches == 0:
        return 0.0

    return min(total_matches / 2, 1.0)


def source_quality_score(url: str) -> float:
    domain = urlparse(url).netloc.lower()
    domain = domain.removeprefix("www.")

    for developer_domain in DEVELOPER_DOMAINS:
        if (
            domain == developer_domain
            or domain.endswith(f".{developer_domain}")
        ):
            return 1.0

    return 0.0


def technical_specificity_score(
    title: str,
    snippet: str | None,
) -> float:
    text = combined_text(title, snippet)

    if not text:
        return 0.0

    matches = 0

    for pattern in TECHNICAL_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            matches += 1

    return min(matches / 2, 1.0)


def query_match_score(
    query: str,
    title: str,
    snippet: str | None,
) -> float:
    query_tokens = tokenize(query)
    title_tokens = tokenize(title)
    snippet_tokens = tokenize(snippet)

    if not query_tokens:
        return 0.0

    title_ratio = (
        len(query_tokens & title_tokens)
        / len(query_tokens)
    )

    snippet_ratio = (
        len(query_tokens & snippet_tokens)
        / len(query_tokens)
    )

    return min(
        0.65 * title_ratio
        + 0.35 * snippet_ratio,
        1.0,
    )


def calculate_relevance(
    product_name: str,
    query: str,
    title: str,
    snippet: str | None,
    url: str,
) -> RelevanceResult:

    product_relevance = product_match_score(
        product_name,
        title,
        snippet,
    )

    developer_relevance = developer_relevance_score(
        title,
        snippet,
    )

    problem_relevance = problem_relevance_score(
        title,
        snippet,
    )

    source_quality = source_quality_score(url)

    technical_specificity = technical_specificity_score(
        title,
        snippet,
    )

    query_relevance = query_match_score(
        query,
        title,
        snippet,
    )

    score = (
        0.25 * product_relevance
        + 0.15 * query_relevance
        + 0.20 * developer_relevance
        + 0.20 * problem_relevance
        + 0.10 * source_quality
        + 0.10 * technical_specificity
    )

    return RelevanceResult(
        score=round(min(score, 1.0), 2),
        product_relevance=round(product_relevance, 2),
        developer_relevance=round(developer_relevance, 2),
        problem_relevance=round(problem_relevance, 2),
        source_quality=round(source_quality, 2),
        technical_specificity=round(
            technical_specificity,
            2,
        ),
    )


def is_relevant(
    score: float,
    threshold: float = 0.40,
) -> bool:
    return score >= threshold