from typing import List

from backend.schema.batch_search_schemas import BatchSearchRequest, BatchSearchResponse
from backend.schema.cd_entry import BatchCdEntry
from backend.service.aligmnemt_parser import AlignmentParser
from backend.service.batch_cdd_scrapper import BatchCddScrapper


class BatchSearchHandler:
    @classmethod
    async def get_search_result(cls, search_id: str) -> List[BatchCdEntry]:
        cds_id = await BatchCddScrapper.get_cdsid_from_search_id(search_id)
        alignment = await BatchCddScrapper.get_alignment_from_cds_id(cds_id)
        return await AlignmentParser.parse(alignment)

    @classmethod
    async def launch_search(cls, batch_search_request: BatchSearchRequest) -> BatchSearchResponse:
        return await BatchCddScrapper.launch_search(batch_search_request)

