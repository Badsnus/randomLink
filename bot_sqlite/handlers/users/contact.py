from aiogram import types

from loader import dp, db


@dp.message_handler(text='Связь')
async def show_contact(message: types.Message):
    await message.answer('По всем вопросам писать: @badsnus')
