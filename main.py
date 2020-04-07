import logging
from os import environ

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types

from bot.keyboards import generate_main_menu
from bot.replicas import REPLICAS
from bot.utils import is_admin

TG_TOKEN = environ["TG_TOKEN"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TG_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    welcome_message = REPLICAS["welcome"].format(message.from_user["first_name"])
    keyboard = generate_main_menu(is_admin(message.from_user["id"]))
    await message.answer(welcome_message, reply_markup=keyboard)


@dp.message_handler(commands=["help"])
async def send_help(message: types.Message):
    await message.answer(REPLICAS["help"])


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(REPLICAS["idk"])


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
