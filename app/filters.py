from aiogram.filters import BaseFilter
from aiogram.enums import ContentType
from aiogram.types import Message


class Text(BaseFilter):
    async def __call__(self, message: Message):
        return message.content_type == ContentType.TEXT
