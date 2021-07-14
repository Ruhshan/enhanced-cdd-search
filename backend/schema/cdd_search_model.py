from pydantic import BaseModel


class CddSearchModel(BaseModel):
    seqinput: str
    db: str
    evalue: float
    compbasedadj: str
    maxhits: int
    lift: str
    suppr: str
    frclive = 'T'
    mode='full'
