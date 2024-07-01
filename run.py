import asyncio

from aiogram import Bot, Dispatcher

from app.config import environment
from app.handlers import router
from app.middleware import UserCheckMiddleware
from app.database import db

# Инициализируем бота и диспетчер
bot = Bot(token=environment["TELEGRAM"])
dp = Dispatcher()

router.message.middleware(UserCheckMiddleware(db))
dp.include_router(router)


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
