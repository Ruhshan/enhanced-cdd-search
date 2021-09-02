from pydantic import BaseModel


class BatchSearchRequest(BaseModel):
    queries: str
    selectedDatabase: str
    eValueThreshold: float
    compositionCorrectedScoring: bool
    applyLowComplexityFilter: bool
    includeRetiredSequences: bool
    maxHit: int


class BatchSearchModel(BaseModel):
    queries: str
    db: str
    evalue: str
    compbasedadj: str
    maxhit: int
    filter: str
    useid1: str
    smode: str


class BatchSearchResponse(BaseModel):
    search_id: str
