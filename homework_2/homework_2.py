import asyncio
import logging
from aiogram import F
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command


BOT_TOKEN = "8706016469:AAHfXH6Ii1kmqn0owrhM8kZVvdUsSYZ_DFg"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"＼[o_o] Whats up {message.from_user.full_name}, how it is going"
    )

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "/start - команда для запуска\n"
        "/help - список команд\n"
        "/about - информация о боте"
    )

@dp.message(Command("about"))
async def cmd_help(message: Message):
    await message.answer(
        f"I'm Bender. I bend girders. That's all I'm programmed to do."
    )

@dp.message(F.text.lower() == "группа")
async def cmd_group(message: Message):
    await message.answer("Your group is 71-1!")

@dp.message(F.text.lower() == "пока")
async def cmd_group(message: Message):
    await message.answer("d[=.=]b See you later, aligator")


# @dp.message(F.from_user.id == 2083176557)
# async def cmd_group(message: Message):
#     await message.answer("Well if it isn't my dad!")


@dp.message()
async def echo(message: Message):
    await message.answer(f"What do you mean \"{message.text}\"???")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())