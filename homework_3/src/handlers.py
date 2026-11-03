from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from src.state import Quiz
from src.questions import QUESTIONS
from src.keyboards import reply_buttons, inline_buttons, play_again

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"＼[o_o] Whats up {message.from_user.full_name}, how it is going",
        reply_markup=reply_buttons
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "/start - команда для запуска\n"
        "/help - список команд",
        reply_markup=inline_buttons
    )

@router.message(F.text == "Корзина")
async def cmd_group(message: Message):
    await message.answer("We should get some beer")

@router.callback_query(F.data == "quiz_start")
async def quiz_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Game ON', show_alert=True)
    await state.update_data(index=0, score=0)
    await state.set_state(Quiz.waiting_answer)
    await callback.message.answer(f"Вопрос 1: {QUESTIONS[0]['q']}")

@router.message(Quiz.waiting_answer)
async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    index = data["index"]
    score = data["score"]

    if message.text.lower() == QUESTIONS[index]['a']:
        score += 1
        await message.answer("Правильно! +1")

    else:
        await message.answer(f"Неверно. Правильный ответ: {QUESTIONS[index]['a']}")

    index += 1
    if index >= len(QUESTIONS):
         await message.answer(f"Game over. Score: {score}/{len(QUESTIONS)}")
         await state.clear()
         await message.answer("play again?", reply_markup=play_again)
         
    else:
        await state.update_data(index=index, score=score)
        await message.answer(f"Вопрос {index + 1}: {QUESTIONS[index]['q']}")

@router.message()
async def echo(message: Message):
    await message.answer(f"What do you mean \"{message.text}\"")