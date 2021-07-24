import aiohttp

from backend.exception.custom_exceptions import CallToNCBIFailed


class AIOClient:
    session = None

    @classmethod
    async def create_session(cls):
        cls.session = aiohttp.ClientSession()

    @classmethod
    async def close_session(cls):
        await cls.session.close()

    @classmethod
    async def post(cls, url, data):
        async with cls.session.post(url, data=data) as response:
            if response.status != 200:
                raise CallToNCBIFailed(str(response.status))
            return await response.text()

    @classmethod
    async def get(cls, url):
        async with cls.session.get(url) as response:
            if response.status != 200:
                raise CallToNCBIFailed(str(response.status))
            return await response.text()
