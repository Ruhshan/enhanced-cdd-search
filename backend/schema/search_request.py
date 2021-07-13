from pydantic import BaseModel


class SearchRequest(BaseModel):
    seqinput: str
    selectedDatabase: str
    eValueThreshold: float
    compositionBasedAdjustment: bool
    rescueBorderLineHits: bool
    suppressWeakOverLappingHits: bool
    maxHit: int
