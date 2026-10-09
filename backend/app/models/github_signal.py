from pydantic import BaseModel


class GitHubSignal(BaseModel):
    source: str = "github"
    source_role: str = "community"

    query: str
    title: str
    url: str

    body: str | None = None
    repository: str

    state: str | None = None

    created_at: str | None = None
    updated_at: str | None = None

    comments: int = 0
    reactions: int = 0