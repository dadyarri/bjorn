# from aiogram.types import ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

# from aiogram.types import InlineKeyboardMarkup
# from aiogram.types import InlineKeyboardButton


def generate_main_menu(is_admin: bool) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    if is_admin:
        kb.row(
            KeyboardButton(text="Призыв"), KeyboardButton(text="Финансы"),
        )
    kb.row(
        KeyboardButton(text="Расписание"), KeyboardButton(text="Рассылки"),
    )
    if is_admin:
        kb.row(KeyboardButton(text="Настройки"))
    return kb
