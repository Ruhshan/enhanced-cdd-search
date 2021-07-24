from typing import List

from fastapi import APIRouter

from backend.schema.batch_search_schemas import BatchSearchResponse, BatchSearchRequest
from backend.schema.search_request import SearchRequest
from backend.schema.search_response import SearchResponse
from backend.service.batch_cdd_scrapper import BatchCddScrapper
from backend.service.search_handler import SearchHandler

router = APIRouter()


@router.post("/new", response_model=SearchResponse)
async def search(search_request: SearchRequest):
    return SearchHandler.new_search(search_request)


@router.post("/batch", response_model=BatchSearchResponse)
async def batch_search(search_request: BatchSearchRequest):
    return await BatchCddScrapper.launch_search(search_request)

