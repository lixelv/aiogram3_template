from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable

from app.database import AsyncDB


class UserCheckMiddleware(BaseMiddleware):
    def __init__(self, db: AsyncDB):
        super().__init__()
        self.db = db

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        if not await self.db.user_exists(event.from_user.id):
            await self.db.add_user(
                event.from_user.id,
                event.from_user.username,
                event.from_user.language_code,
                event.date,
            )

        result = await handler(event, data)
        return result
