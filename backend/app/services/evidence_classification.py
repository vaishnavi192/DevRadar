import re

from app.models.evidence import Evidence
from app.models.evidence_classification import EvidenceClassification


PROBLEM_PHRASES = {
    "problem",
    "error",
    "exception",
    "failed",
    "failure",
    "broken",
    "bug",
    "incorrect",
    "invalid",
    "not working",
    "doesn't work",
    "unable to",
    "cannot",
    "can't",
    "timeout",
}

EDUCATION_PHRASES = {
    "tutorial",
    "step-by-step",
    "how to",
    "quick tour",
    "guide",
    "walkthrough",
}

IMPLEMENTATION_TERMS = {
    "python",
    "javascript",
    "typescript",
    "node",
    "sdk",
    "library",
    "package",
    "code",
    "scraper",
}

INTEGRATION_TERMS = {
    "integration",
    "integrate",
    "n8n",
    "zapier",
    "webhook",
    "workflow",
    "connect",
    "connector",
}


def normalize_text(value: str | None) -> str:
    if not value:
        return ""

    return re.sub(r"\s+", " ", value.lower()).strip()


def contains_phrase(text: str, phrase: str) -> bool:
    """
    Handles both single words and multi-word phrases.
    """
    if " " in phrase:
        return phrase in text

    return re.search(rf"\b{re.escape(phrase)}\b", text) is not None


def classify_evidence(
    evidence: Evidence,
) -> EvidenceClassification:

    title = normalize_text(evidence.title)
    text = normalize_text(evidence.text)

    combined_text = f"{title} {text}"

    evidence_types: list[str] = []

    # -----------------------------------------
    # Problem evidence
    # -----------------------------------------

    # -----------------------------------------
# Problem evidence
# -----------------------------------------

    problem_matches = [
        phrase
        for phrase in PROBLEM_PHRASES
        if contains_phrase(title, phrase)
    ]

    if problem_matches:
        evidence_types.append("problem")

    # -----------------------------------------
    # Education / content evidence
    # -----------------------------------------

    education_matches = [
        phrase
        for phrase in EDUCATION_PHRASES
        if contains_phrase(combined_text, phrase)
    ]

    if education_matches:
        evidence_types.append("education")

    # -----------------------------------------
    # Implementation evidence
    # -----------------------------------------

    implementation_matches = [
        term
        for term in IMPLEMENTATION_TERMS
        if contains_phrase(combined_text, term)
    ]

    if implementation_matches:
        evidence_types.append("implementation")

    # -----------------------------------------
    # Integration evidence
    # -----------------------------------------

    integration_matches = [
        term
        for term in INTEGRATION_TERMS
        if contains_phrase(combined_text, term)
    ]

    if integration_matches:
        evidence_types.append("integration")

    # -----------------------------------------
    # Generic evidence
    # -----------------------------------------

    if not evidence_types:
        evidence_types.append("generic")

    return EvidenceClassification(
        evidence_types=evidence_types
    )