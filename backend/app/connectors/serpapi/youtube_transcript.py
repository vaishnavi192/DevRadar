import os

import serpapi
from dotenv import load_dotenv

load_dotenv()


def get_youtube_transcript(
    video_id: str,
) -> str | None:

    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        raise RuntimeError("SERPAPI_KEY is not configured")

    client = serpapi.Client(
        api_key=api_key
    )

    results = client.search(
        {
            "engine": "youtube_video_transcript",
            "v": video_id,
        }
    )

    return _extract_transcript(results)


def _extract_transcript(
    results: dict,
) -> str | None:

    transcript = results.get("transcript", [])

    if not transcript:
        return None

    parts = []

    for item in transcript:

        if not isinstance(item, dict):
            continue

        text = item.get("snippet")

        if text:
            parts.append(text)

    if not parts:
        return None

    return " ".join(parts)