from pydantic import BaseModel


class EvidenceClassification(BaseModel):
    evidence_types: list[str]