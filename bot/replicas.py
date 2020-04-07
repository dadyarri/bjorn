from aiogram.utils.markdown import text
from aiogram.utils.markdown import bold

# from aiogram.utils.markdown import italic
# from aiogram.utils.markdown import code
# from aiogram.utils.markdown import pre

REPLICAS = {
    "welcome": text(
        "Привет ",
        bold("{0}"),
        "\! Я Бьорн, бот\-помощник для студенческих групп",
        "\n",
        "Ты можешь получить ссылку на документацию, отправив мне команду",
        " /help",
        sep="",
    ),
    "help": "Здесь будет ссылка на документацию...",
    "idk": "Я не понимаю. Отправьте /help, чтобы получить справку по боту",
}
