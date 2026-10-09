from pydantic import BaseModel


class SearchHypothesis(BaseModel):
    key: str
    product_name: str
    query: str
    intent: str
    signal_type: str
    
    