from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from db.users import create_user, get_user

router = Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
    user = create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username or "Anon"
    )
    await message.answer(
        f"this bot is online"
    )