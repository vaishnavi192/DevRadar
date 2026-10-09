from pydantic import BaseModel


class YouTubeSignal(BaseModel):
    source: str = "youtube"
    source_role: str = "community"

    query: str
    video_id: str

    title: str
    url: str
    snippet: str | None = None

    channel: str | None = None
    published_at: str | None = None

    views: int | None = None
    likes: int | None = None
    comments: int | None = None

    transcript: str | None = None
    transcript_available: bool = False

    relevance_score: float = 0.0