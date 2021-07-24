import requests
import re

from backend.exception.custom_exceptions import CallToNCBIFailed, InvalidBatchSearchId


class BatchCddScrapper:
    @classmethod
    def get_cdsid_from_search_id(cls, search_id):
        res = requests.request("GET",
                               "https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi?cdsid={}&tdata=aligns&alnfmt=text&dmode=all".format(
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
