from typing import List

from backend.schema.cd_entry import CdEntry
from backend.schema.cdd_search_model import CddSearchModel
from backend.schema.search_request import SearchRequest
from backend.schema.search_response import SearchResponse
from backend.service.cdd_parser import CddParser
from backend.service.cdd_scrapper import CddScrapper


class SearchHandler:
    @staticmethod
    async def new_search(search_request: SearchRequest) -> SearchResponse:
        search_model = CddSearchModel(
            seqinput=search_request.seqinput,
            db=search_request.selectedDatabase,
            evalue=search_request.eValueThreshold,
            maxhits=search_request.maxHit,
            compbasedadj="T" if search_request.compositionBasedAdjustment else "",
            lift="T" if search_request.rescueBorderLineHits else "",
            suppr="T" if search_request.suppressWeakOverLappingHits else ""
        )

        initial_response = await CddScrapper.initiate(search_model)
        dhandle = await CddParser.extract_dhandle(initial_response)
        fetched_result = await CddScrapper.fetch_result(dhandle)
        data = await CddParser.extract_cdd_entries(fetched_result)
        return SearchResponse(count=len(data), data=data)
