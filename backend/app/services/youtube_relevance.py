def classify_youtube_source(channel: str | None) -> str:

    if not channel:
        return "community"

    normalized = channel.lower().strip()

    if normalized in {
        "serpapi",
        "serpapi, llc",
    }:
        return "first_party"

    return "community"