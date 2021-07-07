from pydantic import BaseModel


class SearchRequest(BaseModel):
    seqinput: str
    db: str
    evalue: float
    compbasedadj: str
    maxhits: int
    frclive = 'T'
    mode='rep'
