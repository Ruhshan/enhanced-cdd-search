import time

from backend.exception.custom_exceptions import CallToNCBIFailed
from backend.schema.cdd_search_model import CddSearchModel

import requests


search_url = "https://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi"


class CddScrapper:
    @staticmethod
    def initiate(search_request: CddSearchModel) -> str:
        response = requests.request("POST", search_url, data=search_request.dict())

        if response.status_code != 200:
            raise CallToNCBIFailed(str(response.status_code))

        return response.text

    @staticmethod
    def fetch_result(dhandle: str) -> str:
        fetch_result_request = {
            "dhandle": dhandle, "output": "html", "wait4blast10": "10", "mode": "rep", "data": "ftable", "gwidth": "-1",
            "loading": "true", "logarch": "true"
        }
        time.sleep(8)
        response = requests.request("POST", search_url, data=fetch_result_request)
        if response.status_code != 200:
            raise CallToNCBIFailed
        return response.text


