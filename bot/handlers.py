from pprint import pprint

from aiogram import Router, F
from aiogram.client.session import aiohttp
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import API_TOKEN, API_URL
from api.service.validator import validate_imei

router = Router()


async def check_imei_api(imei: str) -> dict:
    headers = {"Token": f"{API_TOKEN}"}  # Токен в заголовках
    params = {"imei": imei}
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                    API_URL,
                    headers=headers,
                    params=params
            ) as response:
                if response.status == 200:
                    return await response.json()
        except aiohttp.ClientError as e:
            return {"error": f"Connection error: {str(e)}"}


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Для проверки IMEI введите команду /check IMEI")


@router.message(F.text.startswith('/check'))
async def imei_handler(message: Message):
    imei = message.text.split(' ')
    if len(imei) == 2:
        if validate_imei(imei[1]):
            await message.bot.send_chat_action(message.chat.id, "typing")
            api_response = await check_imei_api(imei[1])
            for info in api_response:
                if len(info["properties"]):
                    if isinstance(info["properties"], dict):
                        await message.answer(info["properties"]["deviceName"])
                        await message.answer(info["properties"]["image"])

        else:
            await message.answer("Введите корректный IMEI")
    else:
        await message.answer("Введите IMEI")
