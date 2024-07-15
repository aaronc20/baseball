import httpx, json

async def get(URL):
    return httpx.get(URL).json()