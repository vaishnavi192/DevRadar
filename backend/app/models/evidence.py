from pydantic import BaseModel


class Evidence(BaseModel):
    source: str
    source_role: str

    title: str
    url: str

    query: str | None = None
    text: str | None = None

    relevance_score: float = 0.0