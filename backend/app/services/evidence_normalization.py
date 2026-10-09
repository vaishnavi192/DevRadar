from app.models.evidence import Evidence
from app.models.github_signal import GitHubSignal
from app.models.signal import Signal
from app.models.youtube_signal import YouTubeSignal
from app.models.research_packet import ResearchPacket

def normalize_google_signal(signal: Signal) -> Evidence:
    return Evidence(
        source=signal.source,
        source_role=signal.source_role,
        title=signal.title,
        url=signal.url,
        query=signal.query,
        text=signal.snippet,
        relevance_score=signal.relevance_score,
    )


def normalize_youtube_signal(signal: YouTubeSignal) -> Evidence:
    text = signal.transcript or signal.snippet

    return Evidence(
        source=signal.source,
        source_role=signal.source_role,
        title=signal.title,
        url=signal.url,
        query=signal.query,
        text=text,
        relevance_score=signal.relevance_score,
    )


def normalize_github_signal(signal: GitHubSignal) -> Evidence:
    return Evidence(
        source=signal.source,
        source_role=signal.source_role,
        title=signal.title,
        url=signal.url,
        query=signal.query,
        text=signal.body,
        relevance_score=signal.relevance_score,
    )



def normalize_research_packet(packet: ResearchPacket) -> list[Evidence]:
    evidence = []

    for signal in packet.google_search:
        evidence.append(normalize_google_signal(signal))

    for signal in packet.youtube:
        evidence.append(normalize_youtube_signal(signal))

    for signal in packet.github:
        evidence.append(normalize_github_signal(signal))

    return evidence