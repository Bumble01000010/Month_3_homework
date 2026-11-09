
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(token="8706016469:AAHfXH6Ii1kmqn0owrhM8kZVvdUsSYZ_DFg")
dp = Dispatcher(storage=MemoryStorage())

async def main():
    init_db()
    db.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())