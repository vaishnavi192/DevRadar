from pydantic import BaseModel


class Product(BaseModel):
    name: str
    website: str
    targetAudience: str
    docs_url: str | None = None
    github_url: str | None = None
    competitors: list[str] = []
    primary_goal: str = "Developer acquisition"