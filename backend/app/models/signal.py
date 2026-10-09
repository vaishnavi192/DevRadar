from pydantic import BaseModel


class Signal(BaseModel):
    source: str
    source_role: str
    signal_type: str
    query: str
    title: str
    url: str
    snippet: str | None = None
    relevance_score: float