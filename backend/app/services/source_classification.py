from urllib.parse import urlparse


FIRST_PARTY_DOMAINS = {
    "serpapi.com",
}

COMMUNITY_DOMAINS = {
    "github.com",
    "stackoverflow.com",
    "reddit.com",
    "youtube.com",
    "dev.to",
    "hashnode.com",
}


def classify_source_role(url: str) -> str:
    domain = urlparse(url).netloc.lower().removeprefix("www.")

    if domain in FIRST_PARTY_DOMAINS or domain.endswith(".serpapi.com"):
        return "first_party"

    for community_domain in COMMUNITY_DOMAINS:
        if domain == community_domain or domain.endswith(f".{community_domain}"):
            return "community"

    return "third_party"