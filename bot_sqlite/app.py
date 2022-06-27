from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):

    await set_default_commands(dispatcher)

    await on_startup_notify(dispatcher)
    db.create_table_users()
    db.create_table_links()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

