from random import choices
from string import ascii_letters, digits

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import host
from loader import dp, db
from keyboards.inline.createLinkKeyboard import create_link_buttons


@dp.message_handler(text='Создать ссылку')
async def ask_link(message: types.Message, state: FSMContext):
    await message.answer('Пришлите ссылки через запятую для рандома\n'
                         'Например:\n'
                         'https://lolz.guru/badsnus/,https://github.com/Badsnus/')
    await state.set_state('get_link')
    await state.update_data({'links': []})


@dp.message_handler(state='get_link')
async def show_links(message: types.Message, state: FSMContext):
    data = await state.get_data()
    old_links = data.get('links')
    links = [i for i in message.text.split(',') if 'https://' in i or 'http://' in i] + old_links
    await state.update_data({'links': links})
    text = 'Пришлите дополнительные ссылки для добавления\n' \
           'Текущие ссылки:\n'
    for link in enumerate(links):
        text += f'{link[0] + 1}.{link[1]}\n'
    await message.answer(text, reply_markup=create_link_buttons, disable_web_page_preview=True)


@dp.callback_query_handler(text_startswith='create_link', state='get_link')
async def verdict_link(call: types.CallbackQuery, state: FSMContext):
    verdict = int(call.data.split('-')[1])
    if verdict == 1:
        data = await state.get_data()
        links = ''
        for link in data.get('links'):
            links += link + ','
        link_name = ''.join(choices(ascii_letters + digits, k=20))
        db.add_link(link_name=link_name, user_id=call.from_user.id, links=links[:-1])
        text = 'Ссылка успешно создана ✅\n' \
               f'Ваша ссылка: <b>{host + link_name}</b>'
    else:
        text = 'Создание ссылки отменено'

    await call.message.edit_text(text)
    await state.finish()