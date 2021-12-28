import os

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.environ.get("BOTTOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def start_event(message: types.Message):
    await message.reply(f"Привет, {message.from_user.first_name}!\nОтправь мнесписок вопросов, на которых ты хочешь тренироваться.\n\nНапример:\n1. Теорема Пифагора\n2. Что такое синус\n3. Имя препода по вышмату")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
