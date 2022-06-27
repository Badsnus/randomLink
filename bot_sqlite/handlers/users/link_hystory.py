from aiogram import types

from data.config import host
from loader import dp, db


def get_links(id):
    links = db.select_links(user_id=id)
    links_text = 'Ваши ссылки:\n'
    markup = types.InlineKeyboardMarkup(row_width=2)
    for link in enumerate(links):
        links_text += f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n' \
                      f'{host}{link[1][0]}\n' \
                      f'Количество посещений: {link[1][3]}\n' \
                      f'Введет на ресурсы: {link[1][2].replace("https://", "").replace("http://", "")}\n' \
                      f'➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
        markup.insert(
            types.InlineKeyboardButton(text=f'Удалить ссылку: {link[1][0]}', callback_data=f'del_link-{link[1][0]}'))
    return links_text, markup


@dp.message_handler(text='Мои ссылки')
async def show_links(message: types.Message):
    links_text, markup = get_links(message.from_user.id)
    await message.answer(links_text, reply_markup=markup)


@dp.callback_query_handler(text_startswith='del_link')
async def delete_link(call: types.CallbackQuery):
    link_name = call.data.split('-')[1]
    db.delete_link(link_name=link_name)
    links_text, markup = get_links(call.from_user.id)
    await call.answer('Ссылка удалена')
    await call.message.edit_text(links_text, reply_markup=markup)
