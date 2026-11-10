from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

router = Router()

#_______________________________________commands_______________________________________________

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer(
        f"＼[o_o] Whats up {message.from_user.full_name}, how it is going"
    )

@router.message(Command("help)"))
async def cmd_help(message:Message):
    await message.answer(
        "/start - starts the bot\n"
        "/help - brings ups the list of all commands"
    )

#________________________________________text_word_filter_______________________________________

@router.message(F.text =="beer")
async def filter_catch_beer(message:Message):
    await message.answer(
        "Did someone say 'Beer'"
    )