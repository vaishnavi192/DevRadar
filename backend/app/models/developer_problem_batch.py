from pydantic import BaseModel

from app.models.developer_problem import DeveloperProblem


class DeveloperProblemBatch(BaseModel):
    problems: list[DeveloperProblem]