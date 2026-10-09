from pydantic import BaseModel, Field


class TrendSignal(BaseModel):
    source: str = "google_trends"
    query: str

    trend_direction: str

    interest_over_time: list[dict] = Field(default_factory=list)
    related_topics: list[str] = Field(default_factory=list)
    related_queries: list[str] = Field(default_factory=list)