from pydantic import BaseModel, Field

from app.models.developer_problem import DeveloperProblem


class DemandSignal(BaseModel):
    query: str
    direction: str
    interpretation: str
    limitations: list[str] = Field(default_factory=list)


class ContentGap(BaseModel):
    topic: str
    reason: str
    evidence: list[str] = Field(default_factory=list)


class GTMRecommendation(BaseModel):
    recommendation: str
    reason: str
    priority: str


class ResearchSynthesis(BaseModel):
    developer_problems: list[DeveloperProblem] = Field(
        default_factory=list
    )

    conclusions: list[str] = Field(
        default_factory=list
    )

    demand_signals: list[DemandSignal] = Field(
        default_factory=list
    )

    content_gaps: list[ContentGap] = Field(
        default_factory=list
    )

    gtm_recommendations: list[GTMRecommendation] = Field(
        default_factory=list
    )