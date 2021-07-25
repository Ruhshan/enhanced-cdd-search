from typing import List

from fastapi import APIRouter

from backend.schema.batch_search_schemas import BatchSearchResponse, BatchSearchModel, BatchSearchRequest
from backend.schema.cd_entry import BatchCdEntry
from backend.schema.search_request import SearchRequest
from backend.schema.search_response import SearchResponse
from backend.service.batch_search_handler import BatchSearchHandler
from backend.service.search_handler import SearchHandler

router = APIRouter()


@router.post("/new", response_model=SearchResponse)
async def search(search_request: SearchRequest):
    return await SearchHandler.new_search(search_request)


@router.post("/batch", response_model=BatchSearchResponse)
async def batch_search(search_request: BatchSearchRequest):
    return await BatchSearchHandler.launch_search(search_request)


@router.get("/batch/{search_id}", response_model=List[BatchCdEntry])
async def batch_result(search_id: str):
    return await BatchSearchHandler.get_search_result(search_id)
