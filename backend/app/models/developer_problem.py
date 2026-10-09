from pydantic import BaseModel, Field


class DeveloperProblem(BaseModel):
    cluster_id: str
    title: str
    conclusion: str
    evidence_count: int
    source_breakdown: dict[str, int]
    confidence: str
    supporting_evidence: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)
    is_problem: bool