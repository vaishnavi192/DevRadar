from app.models.evidence import Evidence


def deduplicate_evidence(
    evidence: list[Evidence],
) -> list[Evidence]:
    seen_urls = set()
    unique = []

    for item in evidence:
        if item.url in seen_urls:
            continue

        seen_urls.add(item.url)
        unique.append(item)

    return unique