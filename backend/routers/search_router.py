from typing import List

from fastapi import APIRouter

from backend.schema.cd_entry import CdEntry
from backend.schema.cdd_search_model import CddSearchModel
from backend.service.cdd_search import CddSearch
from backend.service.extractor import Extractor

router = APIRouter()

@router.get("/", response_model=List[CdEntry])
async def search():
    search_model = CddSearchModel(
        seqinput="",
        db="cdd",
        evalue=0.010000,
        compbasedadj="T",
        maxhits=500,
    )
    initial_response = CddSearch.initiate(search_model)
    dhandle= Extractor.extract_dhandle(initial_response)
    fetched_result = CddSearch.fetch_result(dhandle)

    return Extractor.extract_cdd_entries(fetched_result)