from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from db.users import get_user, create_user

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user = create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username or "Anon"
    )
    await message.answer(
        f"Hi {message.from_user.full_name}, your SQL data: \n{user}",
    )