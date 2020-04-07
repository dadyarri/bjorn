import logging
from os import environ

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types

from aiogram.utils.markdown import text
from aiogram.utils.markdown import bold

# from aiogram.utils.markdown import italic
# from aiogram.utils.markdown import code
# from aiogram.utils.markdown import pre

from bot.utils import is_admin

# from bot.utils import generate_mention

from bot.keyboards import generate_main_menu

TG_TOKEN = environ["TG_TOKEN"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):

    welcome_message = text(
        "Привет ",
        bold(f"{message.from_user['first_name']}"),
        "! Я Бьорн, бот-помощник для студенческих групп",
        "\n",
        "Ты можешь получить ссылку на документацию, отправив мне команду",
        " /help",
        sep="",
    )
    keyboard = generate_main_menu(is_admin(message.from_user["id"]))
    await message.answer(
        welcome_message, parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard
    )


@dp.message_handler(commands=["help"])
async def send_help(message: types.Message):
    help_message = text("Здесь будет ссылка на документацию...")
    await message.answer(
        help_message, parse_mode=types.ParseMode.MARKDOWN,
    )


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(
        "Я не понимаю. Отправьте /help, чтобы получить справку по боту"
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
