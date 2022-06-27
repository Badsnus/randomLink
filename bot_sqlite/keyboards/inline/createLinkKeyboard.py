from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

create_link_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Создать ссылку ✅', callback_data='create_link-1')
    ],
    [
        InlineKeyboardButton('Отменить создание ❌', callback_data='create_link-0')
    ]
])
