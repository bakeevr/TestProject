import aiohttp
from fastapi import HTTPException

from api.service.validator import validate_imei
from config import IMEI_TOKEN


async def imei_check(imei: str) -> list | dict:
    url = "https://api.imeicheck.net/v1/checks"
    if validate_imei(imei):
        try:
            async with aiohttp.ClientSession() as session:
                headers = {"Authorization": f"Bearer {IMEI_TOKEN}"}
                data = {"deviceId": imei}
                async with session.get(url, headers=headers, data=data) as response:
                    return await response.json()
        except HTTPException as e:
            return {"error": str(e)}
    return {"Error": "Неверный формат IMEI"}
