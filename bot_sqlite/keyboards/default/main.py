from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton('Создать ссылку'),
        KeyboardButton('Мои ссылки')
    ],
    [
        KeyboardButton('Связь')
    ]
])