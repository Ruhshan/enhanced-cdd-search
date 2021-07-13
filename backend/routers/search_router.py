from typing import List

from fastapi import APIRouter

from backend.schema.cd_entry import CdEntry
from backend.schema.search_request import SearchRequest
from backend.service.search_handler import SearchHandler

router = APIRouter()


@router.post("/new", response_model=List[CdEntry])
async def search(search_request: SearchRequest):
    return SearchHandler.new_search(search_request)