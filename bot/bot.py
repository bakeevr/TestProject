import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN, allowed_users
from handlers import router
from middleware import CommandWhitelistMiddleware

dp = Dispatcher()

router.message.middleware(CommandWhitelistMiddleware(allowed_users))

dp.include_router(router)


async def main() -> None:
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())