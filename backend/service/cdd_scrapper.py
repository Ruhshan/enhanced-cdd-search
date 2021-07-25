
import asyncio

from backend.schema.cdd_search_model import CddSearchModel
from backend.service.async_http_client import AIOClient

search_url = "https://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi"


class CddScrapper:
    @staticmethod
    async def initiate(search_request: CddSearchModel) -> str:
        return await AIOClient.post(search_url, search_request.dict())

    @staticmethod
    async def fetch_result(dhandle: str) -> str:
        fetch_result_request = {
            "dhandle": dhandle, "output": "html", "wait4blast10": "10", "mode": "rep", "data": "ftable", "gwidth": "-1",
            "loading": "true", "logarch": "true"
        }

        await asyncio.sleep(5)

        return await AIOClient.post(search_url, fetch_result_request)


