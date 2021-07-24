import re

from backend.exception.custom_exceptions import InvalidBatchSearchId, JobIsStillRunning, \
    BatchSearchIdNotFound
from backend.schema.batch_search_request import BatchSearchRequest, BatchSearchResponse
from backend.service.async_http_client import AIOClient


class BatchCddScrapper:
    base_url = "https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi"

    @classmethod
    async def launch_search_async(cls, batch_search_request: BatchSearchRequest):
        response = await AIOClient.post(cls.base_url, batch_search_request.dict())
        search_id = re.search("QM3-qcdsearch-\w+", response)
        if search_id:
            return BatchSearchResponse(search_id=search_id.group(0))
        raise BatchSearchIdNotFound("")

    @classmethod
    async def get_cdsid_from_search_id(cls, search_id) -> str:
        response = await AIOClient.get(f'{cls.base_url}?cdsid={search_id}&tdata=aligns&alnfmt=text&dmode=all')
        try:
            match_search_status = re.search("#status\s\d+", response)

            search_status = re.split("\s", match_search_status.group(0))[-1]

            if search_status != "3":
                raise InvalidBatchSearchId(search_id)

            match_cdsid = re.search("#cdsid\s.*", response)
            return re.split("\s", match_cdsid.group(0))[-1]
        except Exception:
            raise InvalidBatchSearchId(search_id)

    @classmethod
    async def get_alignment_from_cds_id(cls, cds_id) -> str:

        response = await AIOClient.get(f'{cls.base_url}?cdsid={cds_id}&tdata=aligns&alnfmt=text&dmode=all')

        job_is_running = re.search("msg\s+Job\s+is\s+still\s+running", response)

        if job_is_running:
            raise JobIsStillRunning("-".join(cds_id.split("-")[:3]))

        search_status_success = re.search("#status\ssuccess", response)

        if search_status_success is None:
            raise InvalidBatchSearchId(cds_id)

        return response
