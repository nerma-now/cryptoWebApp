import asyncio
import aiohttp
from async_lru import alru_cache

class HTTPClient:
    def __init__(self, base_url: str, api_token: str):
        self._session = aiohttp.ClientSession(base_url=base_url,
                                     headers={
                                        'Accepts': 'application/json',
                                        'X-CMC_PRO_API_KEY': api_token,
                                    })

    async def close(self):
        await self._session.close()

class CMCHTTPClient(HTTPClient):
    @alru_cache(ttl=5)
    async def get_listings(self):
        async with self._session.get('/v1/cryptocurrency/listings/latest') as response:
            try:
                result = await response.json()
                await self._session.close()
                return result['data']
            except Exception as ex:
                return print(ex, response.status)

    @alru_cache(ttl=5)
    async def get_currency_logo(self, id: int):
        async with self._session.get('/v2/cryptocurrency/info',
                                     params={'id': id}
                                     ) as response:
            try:
                result = await response.json()
                await self._session.close()
                return { 'logo': result['data'][str(id)]['logo'] }
            except Exception as ex:
                return print(ex, response.status)

    @alru_cache(ttl=5)
    async def get_currency_info(self, id: int):
        async with self._session.get('/v2/cryptocurrency/info',
                                     params={'id': id}
                                     ) as response:
            try:
                result = await response.json()
                await self._session.close()
                return result['data'][str(id)]
            except Exception as ex:
                return print(ex, response.status)

    @alru_cache(ttl=5)
    async def get_currency(self, id: int):
        async with self._session.get('/v2/cryptocurrency/quotes/latest',
                                    params={'id': id}
                                     ) as response:
            try:
                result = await response.json()
                await self._session.close()
                return result['data'][str(id)]
            except Exception as ex:
                print(ex, response.status)