from app.connectors.serpapi.youtube_search import search_youtube
from app.connectors.serpapi.youtube_transcript import get_youtube_transcript
from app.models.youtube_signal import YouTubeSignal
from app.services.youtube_relevance import classify_youtube_source

MAX_VIDEOS = 5
MAX_TRANSCRIPT_CHARS = 12000


def research_youtube(
    query: str,
    product_name: str,
) -> list[YouTubeSignal]:

    search_results = search_youtube(
        query=query,
        product_name=product_name,
        max_results=10,
    )

    relevant_results = [
        signal
        for signal in search_results
        if signal.relevance_score >= 0.30
    ]

    relevant_results.sort(
        key=lambda signal: signal.relevance_score,
        reverse=True,
    )

    selected = relevant_results[:MAX_VIDEOS]

    enriched = []

    for signal in selected:

        transcript = get_youtube_transcript(
            signal.video_id
        )

        if transcript:
            transcript = transcript[:MAX_TRANSCRIPT_CHARS]
            source_role = classify_youtube_source(signal.channel)

            enriched.append(
                signal.model_copy(
                    update={
                        "source_role": source_role,
                        "transcript": transcript,
                        "transcript_available": transcript is not None,
                    }
                )
            )

    return enriched