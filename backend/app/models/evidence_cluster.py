from pydantic import BaseModel

from app.models.evidence import Evidence


class EvidenceCluster(BaseModel):
    key: str
    evidence: list[Evidence]