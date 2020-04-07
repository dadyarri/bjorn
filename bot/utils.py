from os import environ


def is_admin(_id: int) -> bool:
    """
    Проверяет статус администратора указанного пользователя
    Args:
        _id: Идентификатор пользователя Telegram для проверки

    Returns:
        bool: Статус администратора для указанного пользователя
    """
    admins = map(int, environ["ADMINS"].split(":"))
    return _id in admins


def generate_mention(name: str, _id: int) -> str:
    """
    Генерирует упоминание указанного пользователя
    Args:
        name: Имя пользователя
        _id: Идентификатор пользователя

    Returns:
        str: Строка с упоминанием пользователя
    """
    return f"[{name}](tg://user?id={_id})"
