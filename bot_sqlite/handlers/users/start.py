from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from keyboards.default.main import main_keyboard


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if db.select_user(user_id=message.from_user.id) is None:
        db.add_user(user_id=message.from_user.id)
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=main_keyboard)
