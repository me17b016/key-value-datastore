from httpx import AsyncClient, Response

class HttpClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def _make_request(
        self, method: str, endpoint: str, data: dict = None
    ) -> Response:
        async with AsyncClient() as client:
            url = f"{self.base_url}/{endpoint}"
            response = await client.request(method, url, json=data)
            return response

    async def get(self, endpoint: str) -> Response:
        return await self._make_request("GET", endpoint)

    async def post(self, endpoint: str, data: dict) -> Response:
        return await self._make_request("POST", endpoint, data)

    async def put(self, endpoint: str, data: dict) -> Response:
        return await self._make_request("PUT", endpoint, data)

    async def delete(self, endpoint: str) -> Response:
        return await self._make_request("DELETE", endpoint)