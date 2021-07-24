from pydantic import BaseModel

class BatchSearchRequest(BaseModel):
    queries: str
    db: str
    evalue: str
    compbasedadj: str
    maxhit: int

class BatchSearchResponse(BaseModel):
    search_id: str
