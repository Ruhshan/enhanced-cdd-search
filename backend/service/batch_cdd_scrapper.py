import requests
import re

from backend.exception.custom_exceptions import CallToNCBIFailed, InvalidBatchSearchId, JobIsStillRunning, \
    BatchSearchIdNotFound
from backend.schema.batch_search_request import BatchSearchRequest, BatchSearchResponse


class BatchCddScrapper:
    base_url="https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi"
    @classmethod
    def launch_search(cls, request: BatchSearchRequest) ->BatchSearchResponse:
        res = requests.request("POST", cls.base_url, data=request.dict())

        if res.status_code != 200:
            raise CallToNCBIFailed(str(res.status_code))
        search_id = re.search("QM3-qcdsearch-\w+", res.text)
        if search_id:
            return BatchSearchResponse(search_id=search_id.group(0))

        raise BatchSearchIdNotFound("")


    @classmethod
    def get_cdsid_from_search_id(cls, search_id) -> str:
        res = requests.request("GET",cls.base_url+"?cdsid={}&tdata=aligns&alnfmt=text&dmode=all".format(
                                   search_id))

        if res.status_code != 200:
            raise CallToNCBIFailed(str(res.status_code))
        try:
            match_search_status = re.search("#status\s\d+", res.text)

            search_status = re.split("\s", match_search_status.group(0))[-1]

            if search_status != "3":
                raise InvalidBatchSearchId(search_id)

            match_cdsid = re.search("#cdsid\s.*", res.text)
            return re.split("\s", match_cdsid.group(0))[-1]
        except Exception:
            raise InvalidBatchSearchId(search_id)

    @classmethod
    def get_alignment_from_cds_id(cls, cds_id) -> str:
        res = requests.request("GET",
                               "https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi?cdsid={}&tdata=aligns&alnfmt=text&dmode=all".format(
                                   cds_id))

        if res.status_code != 200:
            raise CallToNCBIFailed(str(res.status_code))

        job_is_running = re.search("msg\s+Job\s+is\s+still\s+running",res.text)

        if job_is_running:
            raise JobIsStillRunning("-".join(cds_id.split("-")[:3]))

        search_status_success = re.search("#status\ssuccess",res.text)

        if search_status_success is None:
            raise InvalidBatchSearchId(cds_id)

        return res.text


