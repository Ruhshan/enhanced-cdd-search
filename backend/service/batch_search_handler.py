from typing import List

import asyncio
from backend.schema.batch_search_schemas import BatchSearchModel, BatchSearchResponse, BatchSearchRequest
from backend.schema.cd_entry import BatchCdEntry
from backend.service.aligmnemt_parser import AlignmentParser
from backend.service.batch_cdd_scrapper import BatchCddScrapper


class BatchSearchHandler:
    @classmethod
    async def get_search_result(cls, search_id: str) -> List[BatchCdEntry]:
        cds_id, cookie = await BatchCddScrapper.get_cdsid_from_search_id(search_id)
        await asyncio.sleep(3000)
        alignment = await BatchCddScrapper.get_alignment_from_cds_id(cds_id, cookie)
        return await AlignmentParser.parse(alignment)

    @classmethod
    async def launch_search(cls, batch_search_request: BatchSearchRequest) -> BatchSearchResponse:
        batch_search_model = BatchSearchModel(
            queries=batch_search_request.queries,
            db=batch_search_request.selectedDatabase,
            evalue=str(batch_search_request.eValueThreshold),
            compbasedadj="T" if batch_search_request.compositionCorrectedScoring else "",
            maxhit=batch_search_request.maxHit,
            filter="T" if batch_search_request.applyLowComplexityFilter else "",
            useid1="T" if batch_search_request.includeRetiredSequences else ""

        )
        return await BatchCddScrapper.launch_search(batch_search_model)

