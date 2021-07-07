from pydantic import BaseModel


class CdEntry(BaseModel):
    accession: str
    description: str
    interval: str
    evalue: str
    sequence: str

    @staticmethod
    def new():
        return CdEntry(accession="",description="",interval="",evalue="",sequence="")
