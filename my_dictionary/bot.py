import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters import CommandStart
import config as cf
from job import *
import os

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cf.token)
dp = Dispatcher()

user_id = cf.user_id

if not os.path.exists("user"):
    os.makedirs("user")

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    if message.chat.type == "private":
        if user_id == message.from_user.id:
            await start(message, bot)

@dp.message(F.text)
async def text(message: types.Message):
    if message.chat.type == "private":
        if user_id == message.from_user.id:
            await message_text(message, bot)

@dp.callback_query(MyCallback.filter(F.foo))
async def my_callback_foo(query: CallbackQuery, callback_data: MyCallback):
        if user_id == query.from_user.id:
            await delete_message(query.from_user.id, bot)
            add_activity(query.from_user.id)
            add_mode(query.from_user.id, "0")

            if callback_data.foo == "dictionary":
                await dictionary(query, callback_data, bot)

            elif callback_data.foo == "dictionary_000":
                await dictionary_000(query, callback_data, bot)

            elif callback_data.foo == "dictionary_001":
                await dictionary_001(query, callback_data, bot)

            elif callback_data.foo == "dictionary_002":
                await dictionary_002(query, callback_data, bot)

            elif callback_data.foo == "add":
                await add(query, callback_data, bot)

            elif callback_data.foo == "add_000":
                await add_000(query, callback_data, bot)

            elif callback_data.foo == "add_001":
                await add_001(query, callback_data, bot)

            elif callback_data.foo == "add_002":
                await add_002(query, callback_data, bot)

            elif callback_data.foo == "add_003":
                await add_003(query, callback_data, bot)

            elif callback_data.foo == "train":
                await train(query, callback_data, bot)

            elif callback_data.foo == "train_000":
                await train_000(query, callback_data, bot)

            elif callback_data.foo == "train_001":
                await train_001(query, callback_data, bot)

            elif callback_data.foo == "train_002":
                await train_002(query, callback_data, bot)

            elif callback_data.foo == "train_003":
                await train_003(query, callback_data, bot)

            elif callback_data.foo == "setting":
                await setting(query, callback_data, bot)

            elif callback_data.foo == "setting_000":
                await setting_000(query, callback_data, bot)

            elif callback_data.foo == "setting_001":
                await setting_001(query, callback_data, bot)

            elif callback_data.foo == "setting_002":
                await setting_002(query, callback_data, bot)

            elif callback_data.foo == "setting_003":
                await setting_003(query, callback_data, bot)

            elif callback_data.foo == "setting_004":
                await setting_004(query, callback_data, bot)

            elif callback_data.foo == "exit":
                await exit(query, callback_data, bot)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())