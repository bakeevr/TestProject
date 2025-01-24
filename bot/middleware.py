from typing import Any, Awaitable, Callable
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject


class CommandWhitelistMiddleware(BaseMiddleware):
    def __init__(self, allowed_ids: list[int]):
        self.allowed_ids = allowed_ids

    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any]
    ) -> Any:
        if not isinstance(event, Message):
            return await handler(event, data)

        text = getattr(event, "text", None)

        if text and text.startswith('/'):
            user_id = event.from_user.id
            if user_id not in self.allowed_ids:
                await event.answer("У вас нет доступа к командам!")
                return

        return await handler(event, data)